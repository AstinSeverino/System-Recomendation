from airflow import DAG
from HelloOperator import HelloOperator
from airflow.operators.python import PythonOperator
from datetime import datetime 

with DAG (
    dag_id="hello_world_probando",
    description="hello world probando",
    start_date= datetime(2025, 4,9 ),
    end_date= datetime(2025, 5,9 )) as dag:
    
    t1 = HelloOperator(task_id="hello",
                       name = "Freddy")
    
    t1