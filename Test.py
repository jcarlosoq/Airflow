# import the libraries
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago



#defining DAG arguments
default_args = {
    'owner': 'Juan Carlos Ortiz',
    'start_date': days_ago(0),
    'email': ['correo@ejemplo.com'],
    'email_on_failure': true,
    'email_on_retry': true,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='ETL_toll_data',
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    description='Apache Airflow Final Assignment'
)

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvzf /home/project/airflow/finalassing/filename.tgz',
    dag=dag
)

extract_data_from_csv = BashOperator(
    
)
