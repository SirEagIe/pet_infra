#!/bin/bash

#systemctl restart xray
cat config.json.template | envsubst > /opt/xray/config.json
rm config.json.template
echo 'vless://'$XRAY_UUID'@'$(curl ifconfig.me)':443/?encryption=none&type=tcp&sni='$FAKE_DOMAIN'&alpn=h2&fp=chrome&flow=xtls-rprx-vision&security=reality&pbk='$XRAY_PUBKEY'#vless_vpn' 
/opt/xray/xray run -c /opt/xray/config.json
