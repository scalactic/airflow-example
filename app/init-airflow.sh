#!/usr/bin/env bash

deleteAdmin() {
    airflow users delete -u admin
}

createAdmin() {
    airflow users create \
      --username admin \
      --password admin \
      --firstname airflow \
      --lastname pipeline \
      --role Admin \
      --email air@flow.org
}

# The Standalone command will initialise the database, make a user, and start all components for you.
# You can find admin password in logs.
airflow standalone &

deleteAdmin
while [ "$?" -ne 0 ]; do
  echo "Can't delete admin user"
  sleep 1
  deleteAdmin
done

createAdmin
while [[ "$?" -ne 0 ]]; do
  echo "admin user is NOT created"
  sleep 1
  createAdmin
done
echo "admin user is created"

sleep infinity