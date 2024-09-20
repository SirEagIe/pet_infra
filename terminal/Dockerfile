FROM debian 

RUN apt -y update
RUN apt -y install novnc python3-websockify python3-numpy expect
RUN apt -y install tigervnc-standalone-server dbus-x11 xterm
RUN apt -y install xfce4
RUN apt -y install git vim nmap sudo

ARG TERMINAL_USER
ARG TERMINAL_USER_PASS
ARG TERMINAL_VNC_PASS

RUN useradd $TERMINAL_USER -s /bin/bash -b /home -p $(perl -e "print crypt('"$TERMINAL_USER_PASS"','sa');")
RUN mkdir /home/$TERMINAL_USER
RUN echo $TERMINAL_USER' ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
RUN chown $TERMINAL_USER:$TERMINAL_USER /home/$TERMINAL_USER
USER $TERMINAL_USER
WORKDIR /home/$TERMINAL_USER/

COPY vncpasswd.sh .
RUN sudo chown $TERMINAL_USER:$TERMINAL_USER vncpasswd.sh
RUN chmod u+x vncpasswd.sh
RUN sudo mv /usr/share/novnc/vnc.html /usr/share/novnc/index.html
RUN ./vncpasswd.sh $TERMINAL_VNC_PASS

COPY entrypoint.sh .
RUN sudo chown $TERMINAL_USER:$TERMINAL_USER entrypoint.sh
RUN chmod u+x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
