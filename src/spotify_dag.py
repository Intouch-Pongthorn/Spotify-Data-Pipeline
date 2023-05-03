from airflow import DAG
from airflow.operators.python import PythonOperator
from main import run_spotify_etl
from datetime import datetime,timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 5, 2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'schedule_interval': '@daily'
}

dag = DAG(
    'spotify_dag',
    default_args=default_args
)

run_etl = PythonOperator(
    task_id='execute_spotify_etl',
    python_callable=run_spotify_etl,
    dag=dag, 
)

run_etl
