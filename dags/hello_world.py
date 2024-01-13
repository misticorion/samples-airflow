from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from hello_world_helper import hello_world

default_args = {
    'owner':'airflow',
    'depends_on_past':False,
    'start_date':days_ago(0,0,0,0,0),
    'email':'me@example.com',   # change this config
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=5)
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='hello world',
    schedule_interval=timedelta(days=1),
)

hello_world_etl=PythonOperator(
    task_id='hello_world_etl',
    python_callable=hello_world,
    dag=dag,
)

hello_world_etl