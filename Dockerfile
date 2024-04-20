# Usa una imagen base de Ubuntu
FROM ubuntu:24.04

# Establece el directorio de trabajo en /app
WORKDIR /app



RUN apt-get update && \
        apt-get install -y apt-transport-https \
        python3-dev \
        python3-setuptools \
        python3-wheel \
        python3-venv \
        python3-pip \
        gcc \
        curl 


COPY . /app

RUN python3 -m venv .venv


RUN /app/.venv/bin/pip install -r requirements.txt

RUN /app/.venv/bin/pip install hnswlib

RUN apt clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# ENV OPENAI_API_KEY=''
EXPOSE 8000

