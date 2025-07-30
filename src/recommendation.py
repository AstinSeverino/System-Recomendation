import pandas as pd
from src.data_extraction import load_raw_data
from src.data_preprocessing import preprocess
from src.model import ContentBasedRecommender
from src.config_env import OUTPUT_PATH

def run_recommendations(track_name: str, top_n: int = 10) -> pd.DataFrame:
    """
    Flujo completo: carga, preprocesa, entrena y genera recomendaciones.
    """
    df = load_raw_data()
    X_scaled, meta = preprocess(df)
    
    model = ContentBasedRecommender()
    model.fit(X_scaled, meta)
    
    recs = model.recommend(track_name, top_n)
    recs.to_csv(OUTPUT_PATH, index=False)
    return recs