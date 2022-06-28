ROM ubuntu:18.04

RUN apt-get update

RUN apt-get -y install wget python3 python-pip

RUN pip install virtualenv

RUN apt-get -y install unzip


RUN mkdir deployment_server
ADD server /deployment_server/
RUN virtualenv /deployment_server/server_env/
RUN /deployment_server/server_env/bin/pip install wheel
RUN /deployment/env/bin/pip install -r /deployment_server/requirements.txt

RUN mkdir deployment_client
ADD wave_apps /deployment_client/
RUN virtualenv /deployment_client/client_env/
RUN /deployment_client/client_env/bin/pip install wheel
RUN /deployment_client/env/bin/pip install -r /deployment_client/requirements.txt

RUN wget https://github.com/h2oai/wave/releases/download/v0.22.0/wave-0.22.0-linux-amd64.tar.gz
RUN mkdir /deployment_client/wave && tar -xvf wave-0.22.0-linux-amd64.tar.gz -C /deployment_client/wave --strip-components 1
RUN chmod +x deployment_client/wave/waved

RUN rm wave-0.22.0-linux-amd64.tar.gz



EXPOSE 10101/tcp
