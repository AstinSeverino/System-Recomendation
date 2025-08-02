from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

# Reutilizamos tu lógica existente
from src.data_extraction import load_raw_data
from src.data_preprocessing import preprocess
from src.model import ContentBasedRecommender

app = FastAPI(title="Song Recommender API")

class RecommendRequest(BaseModel):
    track_name: str
    top_n: int = 10

# ----- Carga del modelo en memoria al arrancar -------------------
@app.on_event("startup")
def startup_event():
    global model
    df = load_raw_data()              # descarga + filtra
    X_scaled, meta = preprocess(df)   # escala e imputa
    model = ContentBasedRecommender()
    model.fit(X_scaled, meta)

# ----- Endpoint ---------------------------------------------------
@app.post("/recommend")
def recommend(req: RecommendRequest):
    try:
        recs = model.recommend(req.track_name, req.top_n)
        # devolvemos lista de dicts (JSON)
        return recs.to_dict(orient="records")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
