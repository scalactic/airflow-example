from datetime import datetime, timedelta
from airflow import DAG
from dags.constants import getBashOperator, getPythonOperator


with DAG(
        dag_id="demo-complex-interval-end",
        start_date=datetime.now() - timedelta(weeks=5),
        end_date=datetime.now() + timedelta(days=2),
        schedule="30 8 2,6,8 * *",
        tags=["demo-complex-interval-end"]
) as dag:
    bashOpr = getBashOperator(task_id="bashOperator", dag=dag)
    pythonOpr = getPythonOperator(task_id="pythonOperator", dag=dag)

    bashOpr >> pythonOpr
