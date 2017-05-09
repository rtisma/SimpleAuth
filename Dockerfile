FROM ubuntu:16.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential libssl-dev && \
  apt-get install -y curl git man vim wget && \
  apt-get install -y python3 python3-dev virtualenv

RUN mkdir -p /srv
WORKDIR /srv

ADD . /srv
RUN virtualenv -p python3 env
RUN source env/bin/activate && pip install -r requirements.txt
RUN chmod +x /srv/run.sh

CMD ["/srv/run.sh"]