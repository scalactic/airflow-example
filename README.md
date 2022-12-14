
`docker build -t airflow-docker .`

`docker run --rm -d -p 8080:8080 --name airflow-docker airflow-docker:latest`

`docker stop airflow-docker`