FROM python:alpine3.7
MAINTAINER PTVX001

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app

WORKDIR /app

COPY ./app /app
RUN adduser -D user
User user
