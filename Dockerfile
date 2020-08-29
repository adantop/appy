# Debian buster-slim (10.1)
FROM debian@sha256:11253793361a12861562d1d7b15b8b7e25ac30dd631e3d206ed1ca969bf97b7d

LABEL maintainer "adn.lancer@gmail.com"

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN echo "deb http://ftp.debian.org/debian buster main non-free contrib" >> /etc/apt/sources.list && \
echo "deb-src http://ftp.debian.org/debian buster main non-free contrib" >> /etc/apt/sources.list && \
echo "deb http://ftp.debian.org/debian buster-updates main contrib non-free" >> /etc/apt/sources.list && \
echo "deb-src http://ftp.debian.org/debian buster-updates main contrib non-free" >> /etc/apt/sources.list

RUN apt-get update && apt-get -yq dist-upgrade && \
apt-get install -yq --no-install-recommends locales && \
apt-get clean && rm -rf /var/lib/apt/lists/* && \
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

ENV SHELL /bin/bash
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN apt-get update && apt-get -yq dist-upgrade && \
apt-get install -yq python3 python3-pip libcairo2-dev pkg-config python3-dev cron rsync && \
apt-get clean && rm -rf /var/lib/apt/lists/*

# Add flaski user for running the service
RUN groupadd appy --gid=1000 && useradd -m appy --uid=1000 --gid=1000 && echo "appy:password" | \
    chpasswd

# data folders and access rights
RUN mkdir -p /appy/.git
RUN chown -R appy:appy /appy

# comment during development
COPY accounts /appy/accounts
COPY templates /appy/templates
COPY __main__.py /appy/__main__.py
COPY requirements.txt /appy/requirements.txt
RUN pip3 install -r /appy/requirements.txt

# Flask port
EXPOSE 5000

# Setup default user, when enter docker container
USER appy:appy
WORKDIR /appy

ENTRYPOINT python3 __main__.py
