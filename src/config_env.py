import os

# Aquí lees variables de entorno (Airflow las puede inyectar)
DATA_PATH = os.getenv("DATA_PATH", "/opt/airflow/data/Spotify_Youtube.csv")
# OUTPUT_PATH = os.getenv("OUTPUT_PATH", "/opt/airflow/data/recomendaciones.csv")
OUTPUT_PATH = "/opt/airflow/dags/system_recomendation/practice/system_recomendation/data/recomendaciones.csv"
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
