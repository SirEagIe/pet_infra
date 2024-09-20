#!/bin/bash

websockify -D --web=/usr/share/webapps/novnc/ 8080 localhost:5901
vncserver :1

tail -f /dev/null
