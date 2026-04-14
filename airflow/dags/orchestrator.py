from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
import sys
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

sys.path.append('/opt/airflow/api_request')
def safe_main_callable():
    from insert_record import main
    return main()
default_args = {
    'start_date': pendulum.datetime(2025, 4,30,tz="UTC"),
}
with DAG(
    dag_id='weather_dbt_orchestrator',
    default_args=default_args,
    schedule=pendulum.duration(minutes=1),
    catchup=False
)  as dag:
    task_1=PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable
    )
    task_2= DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(source = '/home/phongthanh/project_dbt_airflow/dbt/my_project',
                  target='/usr/app',
                  type='bind'),
            Mount(source ='/home/phongthanh/project_dbt_airflow/dbt/profiles.yml',
                  target='/root/.dbt/profiles.yml',
                  type='bind'),
        ],
        network_mode='project_dbt_airflow_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )
    task_1>>task_2
