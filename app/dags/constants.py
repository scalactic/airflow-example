from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models.dag import DAG
from pprint import pprint

macros = {
    "M1_LOGICAL_DATE": "{{ dag_run.logical_date }}",
    "M2_TS": "{{ ts }}",
    "M3_DS": "{{ ds }}",
    "M4_YESTERDAY_DS": "{{ yesterday_ds }}",
    "M4_YESTERDAY_V2": "{{ macros.ds_add(ds, -1) }}",
    "M5_ED_LAST_MONTH": "{{ execution_date.subtract(months=1).strftime('%Y-%m-%d') }}",
    "M6_NED_LAST_MONTH": "{{ next_execution_date.subtract(months=1).strftime('%Y-%m-%d') }}",
    "M6_NED_LAST_MONTH_V2": "{{ (next_execution_date - macros.dateutil.relativedelta.relativedelta(months=1)).strftime('%Y-%m-%d') }}",
    "M7_NED_TWO_MONTHS_AGO": "{{ (next_execution_date - macros.dateutil.relativedelta.relativedelta(months=2)).strftime('%Y-%m-%d') }}",
    "M8_DAG_START_DATE": "{{ dag_run.start_date.strftime('%Y-%m-%d') }}"
}


def getBashOperator(task_id, dag: DAG):
    return BashOperator(
        task_id=task_id,
        dag=dag,
        bash_command="/root/scripts/print.sh ",  # <- space is necessary here
        # https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html#jinja-template-not-found
        env=macros
    )


def print_macros(**kwargs):
    """Print the Airflow context and ds variable from the context."""
    pprint(kwargs)
    return "Whatever you return gets printed in the logs"


def getPythonOperator(task_id, dag: DAG):
    return PythonOperator(
        task_id=task_id,
        dag=dag,
        templates_dict=macros,
        python_callable=print_macros
    )
