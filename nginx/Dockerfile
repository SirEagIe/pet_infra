FROM nginx

RUN apt update
RUN apt install -y cron

RUN rm /etc/nginx/conf.d/default.conf
COPY ./cert/fullchain.cer /etc/ssl/
COPY ./cert/privkey.key /etc/ssl/

ARG CONF_FILE
COPY $CONF_FILE /etc/nginx/templates/

RUN rm /usr/share/nginx/html/index.html
COPY ./welcome_page/index.html /usr/share/nginx/html
COPY ./welcome_page/music.mp3 /usr/share/nginx/html

ARG DOMAIN
ARG NEWS_SUBDOMAIN
RUN sed -i 's/NEWS_SUBDOMAIN.DOMAIN/'$NEWS_SUBDOMAIN'.'$DOMAIN'/g' /usr/share/nginx/html/index.html

RUN mkdir /etc/scripts
COPY check_ssl.sh /etc/scripts
RUN chmod +x /etc/scripts/check_ssl.sh
RUN echo "0 10 * * * root /etc/scripts/check_ssl.sh" >> /etc/crontab