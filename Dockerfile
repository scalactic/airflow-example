FROM python:3.10-slim

RUN apt-get update && apt-get install vim -y

WORKDIR /root

ENV AIRFLOW_VERSION=2.6.3
ENV PYTHON_VERSION=3.10
ENV CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
ENV AIRFLOW_HOME=~/airflow

RUN pip install ipython python-dateutil
RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

COPY app/. .
COPY app/dags airflow/dags/dags
RUN rm -r dags

RUN cat bashrc >> .bashrc

ENTRYPOINT ["bash", "init-airflow.sh"]