import requests
import xml.etree.ElementTree as ET
import re
import psycopg2
import random
import os
from time import sleep
from bs4 import BeautifulSoup


rss_feeds = [
    'https://dtf.ru/rss/',
#    'https://lenta.ru/rss',
#    'https://ria.ru/export/rss2/archive/index.xml',
    'https://habr.com/ru/rss/all/all/?fl=ru',
#    'https://russian.rt.com/rss',
#    'https://www.rt.com/rss/',
#    'https://www.rt.com/rss/business/',
#    'https://www.rt.com/rss/pop-culture/',
    'https://rss.stopgame.ru/rss_news.xml',
    'https://xakep.ru/feed/',
    'https://www.securitylab.ru/_services/export/rss/',
    'https://www.ixbt.com/live/rss/',
    'https://wtf.roflcopter.fr/rss-bridge/?action=display&bridge=TelegramBridge&username=%40ru2ch&format=Mrss',
]

conn = psycopg2.connect(dbname=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'], host='pg_db', port=os.environ['POSTGRES_PORT'])
cursor = conn.cursor()

cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS articles (
        id INT GENERATED ALWAYS AS IDENTITY,
        title varchar(1024) NULL,
        description varchar(2048) NULL,
        link varchar(2048) NULL,
        pubDate timestamp NULL,
        image varchar(2048) NULL,
        rss_feed varchar(1024) NULL
    );
    """
)

def normalize_description(description: str):
    description = description.replace('    ', '')
    description = description.replace('\n', '')
    description = description.replace("'", "")
    description = re.sub(r'<.*?>', '', description)
    description = re.sub(r'&.*?;', '`', description)
    return description.strip()

while 1:
    print('==start==')
    for rss_feed in rss_feeds:
        try:
            print(rss_feed)
            response = requests.get(rss_feed)
            with open('/tmp/temp.xml', 'w', encoding="utf-8") as file:
                file.write(response.text)
            xml_tree = ET.parse('/tmp/temp.xml')
            print('start items')
            for item in xml_tree.findall('channel/item'):
                link = item.find('link').text
                cursor.execute(
                    f"""
                    SELECT
                        *
                    FROM
                        articles
                    WHERE
                        link='{link}'
                    """
                )
                if cursor.fetchall():
                    continue

                title = item.find('title')
                if not title is None:
                    title = title.text.replace("'", "")
                    title = re.sub(r'&.*?;', '`', title)
                else:
                    title = "Title"
                description = item.find('description')
                if not description:
                    description = normalize_description(title)
                else:
                    description = normalize_description(description.text)
                pubDate = item.find('pubDate').text
                enclosure = item.find('enclosure')
                if enclosure is None:
                    enclosure = ''
                    i = 0 
                    while not enclosure or 'youtube' in enclosure or 'mp4' in enclosure or i < 10:
                        try:
                            r = requests.get(f'https://www.bing.com/images/search?q={title}')
                            soup = BeautifulSoup(r.text, "html.parser")
                            images = soup.find_all('a', class_='iusc')
                            image = images[random.randint(0, len(images) - 1)]
                            enclosure = re.findall(r'"turl":"(.*?)"', str(image))[0]
                            i += 1
                        except:
                            i += 1
                            continue
                    if not enclosure:
                        enclosure = 'https://www.rbs.ca/wp-content/themes/rbs/images/news-placeholder.png'
                else:
                    enclosure = enclosure.attrib['url']
                print(f'{pubDate} -- {title}, {enclosure}')
                cursor.execute(
                f"""
                    INSERT INTO
                        articles (title, description, link, pubDate, image, rss_feed)
                    VALUES
                        ('{title[:1024]}', '{description[:1024]}', '{link[:1024]}', '{pubDate}', '{enclosure}', '{rss_feed}')
                    """
                )
                conn.commit()
        except:
            continue
    print('==end==')
    cursor.execute(
        f"""
        DELETE FROM articles
        WHERE pubDate < now() - interval '30 days'
        """
    )
    conn.commit()
    sleep(300)
