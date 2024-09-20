FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./cert/fullchain.cer /etc/ssl/
COPY ./cert/privkey.key /etc/ssl/

COPY nginx.conf /etc/nginx/nginx.conf
#RUN sed -i 's/example.com/'$DOMAIN'/g' /etc/nginx/nginx.conf

ARG CONF_FILE
COPY $CONF_FILE /etc/nginx/templates/
COPY nginx_stream.conf.template /etc/nginx/templates/

RUN rm /usr/share/nginx/html/index.html
COPY ./welcome_page/index.html /usr/share/nginx/html
COPY ./welcome_page/music.mp3 /usr/share/nginx/html
COPY htpasswd /etc/nginx/.htpasswd

ARG DOMAIN
ARG NEWS_SUBDOMAIN
RUN sed -i 's/NEWS_SUBDOMAIN.DOMAIN/'$NEWS_SUBDOMAIN'.'$DOMAIN'/g' /usr/share/nginx/html/index.html

