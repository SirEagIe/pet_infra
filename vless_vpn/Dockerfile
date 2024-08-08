FROM ubuntu

RUN apt update
RUN apt install -y curl wget unzip git vim gettext-base 

COPY config.json config.json.template
COPY entrypoint.sh .
RUN chmod +x /entrypoint.sh

RUN wget https://github.com/XTLS/Xray-core/releases/download/v1.8.23/Xray-linux-64.zip
RUN unzip ./Xray-linux-64.zip -d /opt/xray
RUN chmod +x /opt/xray/xray

ENTRYPOINT ["/entrypoint.sh"]
