from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from dags.constants import getBashOperator, getPythonOperator

# A DAG represents a workflow, a collection of tasks
with DAG(
        dag_id="demo-minutes",
        start_date=datetime.now() - timedelta(minutes=5),  # Timezone is UTC.
        end_date=datetime.now() + timedelta(days=2),
        schedule="* * * * *",
        tags=["demo-minutes"]
) as dag:
    bashOpr = getBashOperator(task_id="bashOperator", dag=dag)
    pythonOpr = getPythonOperator(task_id="pythonOperator", dag=dag)


    @task()
    def airflow():
        print("airflow")


    # Set dependencies between tasks
    bashOpr >> pythonOpr >> airflow()
