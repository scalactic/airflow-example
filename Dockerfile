FROM python:3.8-slim

RUN apt-get update && apt-get install vim

WORKDIR /root

COPY .bashrc .
COPY install-airflow.sh .

RUN pip install ipython

ENV AIRFLOW_HOME=~/airflow
ENV TZ=Europe/Istanbul

CMD airflow standalone