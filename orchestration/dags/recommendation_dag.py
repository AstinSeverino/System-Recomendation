import os, sys
# __file__ → .../orchestration/dags/recommendation_dag.py
dag_folder = os.path.dirname(__file__)               # …/orchestration/dags
project_root = os.path.abspath(os.path.join(dag_folder, '..', '..'))  
# project_root → …/system_recomendation
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.utils import setup_logging
from src.recommendation import run_recommendations

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='recommendation_cosine_similarity',
    default_args=default_args,
    description='Pipeline de recomendaciones basadas en Cosine Similarity',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    setup_log = PythonOperator(
        task_id='setup_logging',
        python_callable=setup_logging
    )

    generate_recs = PythonOperator(
        task_id='generate_recommendations',
        python_callable=run_recommendations,
        op_kwargs={'track_name': 'NombreEjemplo', 'top_n': 10}
    )

    setup_log >> generate_recs
