FROM        python:3.7-alpine

RUN         apk update
RUN         apk add --virtual build-dependencies build-base gcc

RUN         mkdir /app
RUN         runtest.py
ADD         requirements.txt /app
RUN         pip install -r /app/requirements.txt
RUN         apk del build-dependencies
ADD         app.py /app

ENTRYPOINT  ["python", "/app/app.py"]
