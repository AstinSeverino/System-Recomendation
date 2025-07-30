import pandas as pd
from src.config_env import DATA_PATH

def load_raw_data(path: str = DATA_PATH) -> pd.DataFrame:
    """
    Carga el CSV de canciones y devuelve un DataFrame.
    """
    df = pd.read_csv(path)
    return df
