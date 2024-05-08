FROM archlinux

RUN pacman --noconfirm -Syu
RUN pacman -S --noconfirm git vim nmap base-devel
RUN pacman -S --noconfirm python3 expect python-numpy
RUN pacman -S --noconfirm tigervnc
RUN pacman -S --noconfirm sudo
RUN pacman -S --noconfirm i3
RUN pacman -S --noconfirm xterm

ARG TERMINAL_USER
ARG TERMINAL_USER_PASS
ARG TERMINAL_VNC_PASS

RUN useradd $TERMINAL_USER -s /bin/bash -b /home -p $(perl -e "print crypt('"$TERMINAL_USER_PASS"','sa');")
RUN mkdir /home/$TERMINAL_USER
RUN echo $TERMINAL_USER' ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
RUN chown $TERMINAL_USER:$TERMINAL_USER /home/$TERMINAL_USER
USER $TERMINAL_USER
WORKDIR /home/$TERMINAL_USER/
RUN git clone https://aur.archlinux.org/yay-bin.git
WORKDIR /home/$TERMINAL_USER/yay-bin
RUN makepkg -si --noconfirm
RUN yay --noconfirm
RUN yay -S --noconfirm novnc 
RUN yay -S --noconfirm websockify
WORKDIR /home/$TERMINAL_USER
RUN rm -r yay-bin
COPY vncpasswd.sh .
RUN sudo chown $TERMINAL_USER:$TERMINAL_USER vncpasswd.sh
RUN chmod u+x vncpasswd.sh
RUN sudo mv /usr/share/webapps/novnc/vnc.html /usr/share/webapps/novnc/index.html
RUN ./vncpasswd.sh $TERMINAL_VNC_PASS

COPY entrypoint.sh .
RUN sudo chown $TERMINAL_USER:$TERMINAL_USER entrypoint.sh
RUN chmod u+x entrypoint.sh

RUN echo 'geometry=1280x720' > ~/.vnc/config
RUN echo 'localhost' >> ~/.vnc/config
RUN echo 'alwaysshared' >> ~/.vnc/config

RUN echo '#!/bin/sh' > ~/.vnc/xstartup
RUN echo 'unset SESSION_MANAGER' >> ~/.vnc/xstartup
RUN echo 'exec i3' >> ~/.vnc/xstartup
RUN chmod +x ~/.vnc/xstartup

ENTRYPOINT ["./entrypoint.sh"]
