
import matplotlib.pyplot as plt
import pandas as pd
def sarima_train_res_stat(test_ts,train_ts,sarima_train_res):
    sarima_pred = sarima_train_res.forecast(len(test_ts))

    plt.figure(figsize=(16,6))

    plt.plot(train_ts.index, train_ts, label="Train", alpha=0.5)
    plt.plot(test_ts.index, test_ts, label="Real (Test)", color="green", linewidth=2)
    plt.plot(test_ts.index, sarima_pred, label="Predicción SARIMA", color="red", linewidth=2)

    plt.title("SARIMA: Predicción vs Valores Reales", fontsize=14)
    plt.xlabel("Fecha")
    plt.ylabel("Demanda por hora")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

    comparison_sarima = pd.DataFrame({
        "Real": test_ts,
        "Predicción SARIMA": sarima_pred,
        "Error Absoluto": (test_ts - sarima_pred).abs()
    })

    return comparison_sarima.head(20)

def graficar_forecast_veinticuatro_horas(ts,res_full,train_ts,test_ts,pred):
    forecast_24 = res_full.forecast(steps=24)
    plt.figure(figsize=(14,5))
    plt.plot(ts.index[-200:], ts[-200:], label="Últimos valores reales")
    plt.plot(pd.date_range(ts.index[-1], periods=24, freq='H'),
            forecast_24, label="Pronóstico 24h", color="orange")

    plt.title("Pronóstico ARIMA para las próximas 24 horas")
    plt.xlabel("Fecha")
    plt.ylabel("Demanda por hora")
    plt.legend()
    plt.show()

    plt.figure(figsize=(16,6))

    plt.plot(train_ts.index, train_ts, label="Train", alpha=0.5)
    plt.plot(test_ts.index, test_ts, label="Real (Test)", color="green", linewidth=2)
    plt.plot(test_ts.index, pred, label="Predicción ARIMA", color="red", linewidth=2)

    plt.title("Comparación Completa de Real vs Predicción (Test)", fontsize=14)
    plt.xlabel("Fecha")
    plt.ylabel("Demanda por hora")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

    error_abs = (test_ts - pred).abs()

    plt.figure(figsize=(16,5))
    plt.plot(error_abs.index, error_abs, color="purple")
    plt.title("Error Absoluto por Hora en el Conjunto de Test")
    plt.xlabel("Fecha")
    plt.ylabel("Error Absoluto")
    plt.grid(alpha=0.3)
    plt.show()

    comparison_detailed = pd.DataFrame({
        "Real": test_ts,
        "Predicción": pred,
        "Error Absoluto": (test_ts - pred).abs()
    })

    return comparison_detailed.head(20)