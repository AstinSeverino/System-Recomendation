# import os

# # Aquí lees variables de entorno (Airflow las puede inyectar)
# # DATA_PATH = os.getenv("DATA_PATH", "/opt/airflow/data/Spotify_Youtube.csv")
# # en config_env.py o directamente en tu script
# DATA_PATH = os.getenv(
#   "DATA_PATH",
#   "/opt/airflow/dags/system_recomendation/practice/system_recomendation/data/Spotify_Youtube.csv"
# )

# # DATA_PATH = "system_recomendation/data/Spotify_Youtube.csv"
# # OUTPUT_PATH = os.getenv("OUTPUT_PATH", "/opt/airflow/data/recomendaciones.csv")
# OUTPUT_PATH = os.getenv("OUTPUT_PATH", "/opt/airflow/dags/system_recomendation/practice/system_recomendation/data/recomendaciones.csv")
# MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")

# system_recomendation/config_env/config_env.py
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]               # …/system_recomendation
DATA_PATH   = os.getenv("DATA_PATH",  str(ROOT_DIR / "data" / "Spotify_Youtube.csv"))
# OUTPUT_PATH = os.getenv("OUTPUT_PATH", str(ROOT_DIR / "data" / "recomendaciones.csv"))
OUTPUT_PATH = "/opt/airflow/dags/system_recomendation/practice/system_recomendation/data/recomendaciones.csv"
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
