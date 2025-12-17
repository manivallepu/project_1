from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from common.utils import greet
 
def say_hello():
    print(greet("Airflow"))
 
with DAG(
    dag_id="example_dag",
    start_date=datetime(2025, 12, 17),
    schedule_interval=None,
    catchup=False
) as dag:
    task = PythonOperator(
        task_id="say_hello_task",
        python_callable=say_hello
    )