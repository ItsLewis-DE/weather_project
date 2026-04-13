from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
import sys
sys.path.append('/opt/airflow/api_request')
def safe_main_callable():
    from insert_record import main
    return main()
default_args = {
    'start_date': pendulum.datetime(2025, 4,30,tz="UTC"),
}
with DAG(
    dag_id='orchestrator',
    default_args=default_args,
    schedule=pendulum.duration(minutes=1),
    catchup=False
)  as dag:
    task_1=PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable
    )
