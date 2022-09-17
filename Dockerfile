FROM python:3.8.3-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD ./ /app


RUN pip install --upgrade pip

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

RUN pip install -r requirements_Docker.txt

COPY ./requirements_Docker.txt /tmp/
RUN cd /tmp && pip install -user -r requirements_Docker.txt