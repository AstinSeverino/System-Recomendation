
import logging
import pandas as pd
from src.config_env import DATA_PATH

def load_raw_data(path: str = DATA_PATH) -> pd.DataFrame:
    """
    Devuelve un DataFrame leyendo, en este orden:
    1) KaggleHub (Spotify & YouTube)   -> Spotify_Youtube.csv
    2) CSV local (si Kaggle falla o no hay credenciales)
    """
    try:
        import kagglehub
        from kagglehub import KaggleDatasetAdapter

        # ⬅️  ¡Sin “data/” delante!
        file_path = "Spotify_Youtube.csv"

        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "salvatorerastelli/spotify-and-youtube",
            file_path,
            # version=1,            # opcional: fuerza la v1
            # force_download=True    # opcional: fuerza nueva descarga
        )
        logging.info("Dataset descargado vía KaggleHub")
        # df.dropna( inplace=True)
        df.dropna(inplace=True)
        df.reset_index(drop=True, inplace=True)
        logging.info(f"Dataset cargado con {len(df)} registros.")
        return df

    except Exception as e:
        logging.warning(f"KaggleHub falló ({e}). Usando CSV local: {path}")
        return pd.read_csv(path)
