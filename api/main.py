from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os, requests, time, json, pathlib

AIRFLOW_API  = os.getenv("AIRFLOW_API", "http://airflow-webserver:8080/api/v1")
AIRFLOW_USER = os.getenv("AIRFLOW_USER", "airflow")
AIRFLOW_PWD  = os.getenv("AIRFLOW_PWD",  "airflow")
RESULT_DIR   = pathlib.Path("/app/data/results")      # donde tu DAG guarda el CSV/JSON

class RecommendRequest(BaseModel):
    track_name: str
    top_n: int = 10

app = FastAPI(title="Song Recommender API")

def trigger_dag(req: RecommendRequest) -> str:
    url  = f"{AIRFLOW_API}/dags/recommendation_cosine_similarity/dagRuns"
    data = {"conf": req.model_dump()}   # {"track_name": ..., "top_n": ...}
    r = requests.post(url, auth=(AIRFLOW_USER, AIRFLOW_PWD), json=data, timeout=10)
    if r.status_code != 200:
        raise HTTPException(500, f"Airflow API error: {r.text}")
    return r.json()["dag_run_id"]

def wait_for_finish(dag_run_id: str, timeout_s=600) -> None:
    url = f"{AIRFLOW_API}/dags/recommendation_cosine_similarity/dagRuns/{dag_run_id}"
    start = time.time()
    while time.time() - start < timeout_s:
        s = requests.get(url, auth=(AIRFLOW_USER, AIRFLOW_PWD), timeout=5).json()
        state = s["state"]
        if state == "success":
            return
        if state in {"failed", "error"}:
            raise HTTPException(500, f"DAG terminó con estado {state}")
        time.sleep(5)
    raise HTTPException(504, "Timeout esperando al DAG")

@app.post("/recommend")
def recommend(req: RecommendRequest):
    dag_run_id = trigger_dag(req)
    wait_for_finish(dag_run_id)
    result_path = RESULT_DIR / f"{dag_run_id}.json"
    if result_path.exists():
        return json.loads(result_path.read_text("utf-8"))
    raise HTTPException(500, "No se encontró el resultado")
