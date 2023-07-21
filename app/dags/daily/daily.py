from datetime import datetime, timedelta
from airflow import DAG
from dags.constants import getBashOperator, getPythonOperator


with DAG(
        dag_id="demo-daily",
        start_date=datetime.now() - timedelta(days=5),
        end_date=datetime.now() + timedelta(days=2),
        schedule="0 12 * * *",
        tags=["demo-daily"]
) as dag:
    bashOpr = getBashOperator(task_id="bashOperator", dag=dag)
    pythonOpr = getPythonOperator(task_id="pythonOperator", dag=dag)

    bashOpr >> pythonOpr
