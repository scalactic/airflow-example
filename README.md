# Airflow Macros Demo
An example demo showing the usage of Airflow macros.
airflow web ui: [localhost:8080](http://localhost:8080)

user: `admin`

password: `admin`

## How to build ?
`docker build -t airflow-docker .`

## How to run ?
`docker run --rm -d -p 8080:8080 --name airflow-docker airflow-docker:latest`

## How to see logs ?
`docker logs airflow-docker -f`

## How to stop ?
`docker stop airflow-docker`

## Example Operators Used in Project
- BashOperator
- PythonOperator
- ShortCircuitOperator
