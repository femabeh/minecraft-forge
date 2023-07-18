FROM ubuntu

LABEL maintainer="femabeh@endkind.net"

WORKDIR /minecraft

RUN apt-get update && apt-get install -y apt-transport-https

RUN apt install -y openjdk-17-jre wget curl python3 python3-pip

RUN pip3 install bs4 requests

ENV FORGEVERSION=recommended

COPY startup/* /minecraft

RUN python3 firststartup.py

ENTRYPOINT ["/bin/bash", "-c", "source /minecraft/run.sh"]
