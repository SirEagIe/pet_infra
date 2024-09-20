#!/bin/bash

tigervncserver -xstartup /usr/bin/startxfce4 -geometry 1600x900 -localhost no :1
websockify -D --web=/usr/share/novnc/ 8080 localhost:5901

tail -f /dev/null
