FROM python:3.12.2

RUN apt-get update -y --fix-missing \
    && apt-get install -y --no-install-recommends \
    sudo \
    vim \
    git \
    curl \
    wget \
    less \
    locate

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
