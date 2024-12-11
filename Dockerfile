FROM python:3.12-alpine3.19

COPY ./app  ./app
COPY ./requirements.txt ./app/requirements.txt

WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /app/requirements.txt && \
    adduser --disabled-password --no-create-home django-user && \
    mkdir -p /usr/src/app/media /usr/src/app/static && \
    chmod -R 755 /app 

ENV PATH="/app:/py/bin:$PATH"

USER  django-user