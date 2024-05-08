from flask import Flask, render_template, request, abort
from PIL import Image
import psycopg2
import datetime
import random
import os


app = Flask(__name__)


@app.route('/kek')
def hello_world():
    return '<h1>ZaLuPa KoNyA</h1><img src="https://cdn-st1.rtr-vesti.ru/vh/pictures/xw/217/453/4.jpg">'


@app.route('/ivleeva_weight')
def ivleeva_weight():
    return f'<h4>Вес Ивлеевой на {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: {random.randint(30, 100)}кг</h4><br><span>(страница создана по просьбе Влада)</span>'


@app.route('/ascii', methods=['GET', 'POST'])
def ascii_art():
    if request.method == 'GET':
        return '''
        <FORM method="post" enctype="multipart/form-data">
                <input type="file" value="image" name="image"/>
                <input type="text" value="1" name="scale"/>
                <input type="submit" value="Submit"/>
        </FORM>
        '''
    if request.method == 'POST':
        image = request.files['image']
        scale = int(request.form.get('scale'))
        #grad = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
        grad = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,"^`\'.'
        img=Image.open(image.stream)
        pixelData = img.load()
        r = ''
        for i in range(0, img.size[1], scale):
            for j in range(0, img.size[0], scale):
                g=(pixelData[j,i][0]+pixelData[j,i][1]+pixelData[j,i][2])//3
                r += grad[g*(len(grad)-1)//255]
            r += '<br>'
        return f'<div style="color:#FFF;font-family: Consolas;">{r}</div><style>body {"{background-color:#000;}"}</style>'


@app.route('/')
def test_db():
    try:
        page = request.args.get('page', default=1, type=int)
        conn = psycopg2.connect(dbname=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'], host='pg_db', port=os.environ['POSTGRES_PORT'])
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM articles ORDER BY pubdate DESC LIMIT 100 OFFSET {(page - 1) * 100}")
        articles = cur.fetchall()
        return render_template('index.html', articles=articles, page=page, request=request)
    except:
        return render_template('index.html', articles=[], page=1, request=request)


if __name__ == '__main__':
    app.run('0.0.0.0')
