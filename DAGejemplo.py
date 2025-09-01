# Librerias
from datetime import timedelta
from airflow.models import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator

#Argumentos del DAG

# Se pueden sobrecargar en cada tarea durante la inicializacion del operador
default_args = {
    'owner': 'Dueño',
    'start_date': days_ago(0),
    'email': ['correo@ejemplo.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definicion del DAG
dag = DAG(
    dag_id='DAG_id',
    default_args=default_args,
    description='A simple description of what the DAG does',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# Tarea con BashOperator
tarea1 = BashOperator(
    task_id='TareaBash',
    bash_command='<comando bash>',
    dag=dag,
)

# Tarea con PythonOperator
tarea2 = PythonOperator(
    task_id='tarea_python',
    python_callable=<funcion python a llamar>,
    dag=dag,
)

# Tarea con EmailOperator
tarea3 = EmailOperator(
    task_id='tarea_correo',
    to='destino@ejemplo.com',
    subject='Ejemplo de correo con Airflow',
    html_content='<p>Correo enviado desde Airflow.</p>',
    dag=dag,
)

#Orden del pipeline
tarea1 >> tarea2 >> tarea3

#Otra forma de generar el pipeline
#tarea1.set_downstream(tarea2)
#tarea3.set_upstream(tarea2)
