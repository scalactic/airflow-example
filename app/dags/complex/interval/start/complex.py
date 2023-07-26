from datetime import datetime, timedelta
from dags.constants import getBashOperator, getPythonOperator, macros
from airflow.operators.python import ShortCircuitOperator
from airflow import DAG
from pprint import pprint


with DAG(
        dag_id="demo-complex-interval-start",
        start_date=datetime.now() - timedelta(weeks=4),
        end_date=datetime.now() + timedelta(days=2),
        schedule="30 8 * * *",
        tags=["demo-complex-interval-start"]
) as dag:
    def short_circuit(**context):
        pprint(context)
        return True if str(context['next_execution_date_day']) in context['schedule_dates'] else False

    bashOpr = getBashOperator(task_id="bashOperator", dag=dag)
    skipOpr = ShortCircuitOperator(
        task_id="skipOpr",
        python_callable=short_circuit,
        templates_dict=macros,
        op_kwargs={
            "next_execution_date_day": "{{ next_execution_date.day }}",
            "schedule_dates": ["2", "6", "8"],
        },
        dag=dag
    )
    pythonOpr = getPythonOperator(task_id="pythonOperator", dag=dag)
    bashOpr >> skipOpr >> pythonOpr
