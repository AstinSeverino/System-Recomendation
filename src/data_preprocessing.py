import pandas as pd
from sklearn.preprocessing import StandardScaler
from typing import Tuple

FEATURES = [
    'Danceability', 'Energy', 'Key', 'Loudness', 'Speechiness',
    'Acousticness', 'Instrumentalness', 'Liveness', 'Valence',
    'Tempo', 'Duration_ms', 'Views', 'Likes', 'Comments', 'Stream'
]

def preprocess(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Escala las features y devuelve (X_scaled_df, items_meta_df)
    donde items_meta_df incluye Track, Artist, Album.
    """
    scaler = StandardScaler()
    X = df[FEATURES]
    X_scaled = scaler.fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=FEATURES, index=df.index)

    items_meta = df[['Track', 'Artist', 'Album']].copy()
    return X_scaled_df, items_meta
