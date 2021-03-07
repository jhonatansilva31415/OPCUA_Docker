FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/client 
COPY . .

RUN apt-get update \
    && apt-get -y install netcat \
    && apt-get clean

RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh