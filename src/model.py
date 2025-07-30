import mlflow
import mlflow.sklearn
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from typing import Any

class ContentBasedRecommender:
    """
    Recomendador basado en similitud de coseno.
    """

    def __init__(self):
        self.item_profiles: pd.DataFrame = pd.DataFrame()

    def fit(self, X_scaled: pd.DataFrame, meta: pd.DataFrame) -> None:
        """
        Guarda el perfil de cada item (canción) para luego consultar similitudes.
        """
        self.item_profiles = X_scaled.copy()
        self.item_profiles[['Track','Artist','Album']] = meta[['Track','Artist','Album']]

    def recommend(self, track_name: str, top_n: int = 10) -> pd.DataFrame:
        """
        Dada una track, devuelve las top_n canciones más similares.
        """
        if self.item_profiles.empty:
            raise ValueError("Modelo no entrenado. Ejecuta fit() primero.")
        
        # Encuentra el vector de la canción solicitada
        mask = self.item_profiles['Track'] == track_name
        if not mask.any():
            raise ValueError(f"Track '{track_name}' no encontrada.")
        query_vec = self.item_profiles.loc[mask, self.item_profiles.columns.difference(['Track','Artist','Album'])].values
        
        # Calcula similitud
        sims = cosine_similarity(query_vec, 
                                 self.item_profiles[self.item_profiles.columns.difference(['Track','Artist','Album'])])
        sims = sims.flatten()
        
        # Empaqueta resultados
        results = self.item_profiles.copy()
        results['similarity'] = sims
        results = results[results['Track'] != track_name]  # excluimos la misma
        return results.sort_values(by='similarity', ascending=False).head(top_n)
