#!/bin/bash

date_now=$(date +%s)
date_cert_exp=$(date --date="$(openssl x509 -noout -text -in /etc/ssl/fullchain.cer | head -n 10 | tail -n 1 | awk '{print $4, $5, $6, $7}')" +%s)
days_before_exp=$[($date_cert_exp - $date_now) / 86400]

if [[ $days_before_exp -lt 10 ]]; then
	curl -X POST \
		-H 'Content-Type: application/json' \
		-d '{"chat_id": "'$TG_MONITORING_CHAT_ID'", "text": "Внимание! До окончания действия сертификата для сайта *[.]'$DOMAIN' осталось: '$days_before_exp' days", "disable_notification": true}' \
		https://api.telegram.org/bot$TG_MONITORING_BOT_TOKEN/sendMessage >/dev/null 2>/dev/null
fi
