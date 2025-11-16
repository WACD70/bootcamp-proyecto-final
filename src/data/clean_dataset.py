import pandas as pd

def limpiar_dataset(df):
    """
    Aplica preprocesamiento básico al dataset NY taxi.
    """
    df = df.dropna()

    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

    df = df.sort_values('tpep_pickup_datetime')

    # Nuevas columnas
    df['hour'] = df['tpep_pickup_datetime'].dt.hour
    df['dayofweek'] = df['tpep_pickup_datetime'].dt.dayofweek

    return df