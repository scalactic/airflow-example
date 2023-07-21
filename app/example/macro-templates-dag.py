import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks
with DAG(
        dag_id="demo",
        start_date=datetime.now() - timedelta(minutes=1),  # Timezone is UTC.
        end_date=datetime.now() + timedelta(days=2),
        schedule="* * * * *",
        tags=["demo"]
) as dag:
    macros = {
        "TEMPLATE_TODAY": "{{ ds }}",
        "TEMPLATE_YESTERDAY": "{{ macros.ds_add(ds, -1) }}",
        "TEMPLATE_LAST_MONTH": "{{ next_execution_date.subtract(months=1).strftime('%Y-%m-%d') }}",
        "TEMPLATE_LAST_MONTH_V2": "{{ (next_execution_date - macros.dateutil.relativedelta.relativedelta(months=1)).strftime('%Y-%m-%d') }}",
        "TEMPLATE_TWO_MONTHS_AGO": "{{ (next_execution_date - macros.dateutil.relativedelta.relativedelta(months=2)).strftime('%Y-%m-%d') }}"
    }
    hello = BashOperator(
        task_id="macros",
        bash_command="/root/example/print.sh ",  # <- space is necessary here
        # https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html#jinja-template-not-found
        dag=dag,
        env=macros
    )

    @task()
    def airflow():
        print("airflow")

    # Set dependencies between tasks
    hello >> airflow()
