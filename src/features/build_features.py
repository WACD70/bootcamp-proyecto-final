
import statsmodels.api as sm
import pandas as pd
def entrenar_sarima_feature(train_ts):
    # Entrenar SARIMA solo con el train
    sarima_train_model = sm.tsa.statespace.SARIMAX(
        train_ts,
        order=(1,1,1),
        seasonal_order=(1,1,1,24),
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    return sarima_train_model.fit()