FROM python:3.8-slim

RUN apt-get update && apt-get install vim -y

WORKDIR /root

RUN pip install ipython

COPY app/. .

ENV AIRFLOW_HOME=~/airflow
ENV TZ=Europe/Istanbul

ENTRYPOINT ["bash", "install-airflow.sh"]