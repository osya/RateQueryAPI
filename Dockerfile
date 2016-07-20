FROM ubuntu:latest
MAINTAINER Valeriy Osipov <infp@vosipov.com>

RUN apt-get update && apt-get -y install xinetd telnetd

RUN echo 'root:root' | chpasswd

COPY telnet /etc/xinetd.d/

RUN echo "pts/0" >> /etc/securetty
RUN echo "pts/1" >> /etc/securetty
RUN echo "pts/2" >> /etc/securetty
RUN echo "pts/3" >> /etc/securetty
RUN echo "pts/4" >> /etc/securetty
RUN echo "pts/5" >> /etc/securetty
RUN echo "pts/6" >> /etc/securetty
RUN echo "pts/7" >> /etc/securetty
RUN echo "pts/8" >> /etc/securetty
RUN echo "pts/9" >> /etc/securetty

ENTRYPOINT service xinetd restart && bash

EXPOSE 23
