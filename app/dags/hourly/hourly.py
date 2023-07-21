from datetime import datetime, timedelta
from airflow import DAG
from dags.constants import getBashOperator, getPythonOperator


with DAG(
        dag_id="demo-hourly",
        start_date=datetime.now() - timedelta(hours=5),
        end_date=datetime.now() + timedelta(days=2),
        schedule="0 * * * *",
        tags=["demo-hourly"]
) as dag:
    bashOpr = getBashOperator(task_id="bashOperator", dag=dag)
    pythonOpr = getPythonOperator(task_id="pythonOperator", dag=dag)

    bashOpr >> pythonOpr
