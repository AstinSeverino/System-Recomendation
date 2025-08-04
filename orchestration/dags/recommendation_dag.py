# orchestration/dags/recommendation_dag.py
from airflow.decorators import dag, task
from datetime import datetime
# ← cambia esta línea
# from system_recomendation.src.recommendation import run_recommendations
# import os, sys
# import run_recommendations
# sys.path.append('/opt/airflow/dags/system_recomendation/practice/system_recomendation/src/recommendation.py')  # asegurarse de que src esté en el path

import os, sys
# sys.path.insert(0,
#     os.path.join(
#         os.path.dirname(__file__),             # …/orchestration/dags
#         '..', '..',                            # sube dos niveles
#         'src'                                  # carpeta src
#     )
# )
# from recommendation import run_recommendations
sys.path.insert(
    0,
    "/opt/airflow/dags/system_recomendation/practice/system_recomendation"
)
from src.recommendation import run_recommendations

@dag(
    schedule=None,  # sólo se lanza via API
    start_date=datetime(2024,1,1),
    catchup=False,
)
def recommendation_cosine_similarity():
    @task()
    def generate_recommendations(track_name: str, top_n: int = 10):
        df = run_recommendations(track_name, int(top_n))
        return df[['Track', 'Artist', 'Album', 'similarity']]\
             .to_dict(orient="records")



    # leer directamente de dag_run.conf
    generate_recommendations(
        track_name="{{ dag_run.conf['track_name'] }}",
        top_n="{{ dag_run.conf.get('top_n', 10) }}"
    )

dag = recommendation_cosine_similarity()
