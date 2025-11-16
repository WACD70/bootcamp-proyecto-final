# README – NYC Taxi Demand Prediction

Este proyecto implementa dos enfoques principales para predecir la demanda de taxis en Nueva York:

1. Regresión lineal usando variables derivadas (features) para explicar la demanda.
2. Modelos de series de tiempo (ARIMA y SARIMA) para capturar tendencias y estacionalidad por hora.

Los datos provienen del dataset público NYC Yellow Taxi Trip Records.

## 1. Objetivo del Proyecto

El objetivo es predecir la demanda de taxis por hora utilizando modelos de aprendizaje automático y series de tiempo.

Incluye:
- Limpieza y procesamiento de datos.
- Generación de nuevas variables (features).
- Entrenamiento de un modelo de regresión lineal.
- Construcción de modelos ARIMA y SARIMA.
- Evaluación mediante métricas.
- Comparación visual entre valores reales y predichos.

## 2. Métricas utilizadas

### 2.1. R² (Coeficiente de Determinación)

Se usa en la regresión lineal.

Indica qué proporción de la variabilidad de la demanda es explicada por el modelo.

Interpretación:
- 0.90 o más: excelente
- 0.70 – 0.89: bueno
- 0.50 – 0.69: regular
- Menos de 0: peor que predecir el promedio

En este proyecto la regresión lineal logró:

**R² ≈ 0.89**

### 2.2. MAE (Mean Absolute Error)

Mide el error absoluto promedio entre valores reales y predichos.

`MAE = mean( | y_real − y_pred | )`

### 2.3. RMSE (Root Mean Squared Error)

`RMSE = sqrt( mean( (y_real − y_pred)² ) )`

### 2.4. AIC (Akaike Information Criterion)

Usado para evaluar modelos ARIMA y SARIMA.

Interpretación:
- AIC bajo: mejor calidad del modelo.
- Sirve para comparar configuraciones del modelo entre sí.

## 3. Resultados Principales

### 3.1 Regresión Lineal

**R² ≈ 0.89**

### 3.2 ARIMA (1,1,1)

- Tiende a producir predicciones planas.
- No captura la estacionalidad de 24 horas.
- MAE y RMSE más altos que SARIMA.

### 3.3 SARIMA (1,1,1)(1,1,1,24)

- Captura la estacionalidad diaria.
- Sigue mejor los picos y caídas de demanda.
- Produce errores más bajos que ARIMA simple.

## 4. Visualizaciones incluidas

- Real vs predicción (ARIMA)
- Real vs predicción (SARIMA)
- Zoom de días recientes
- Error absoluto por hora
- Pronóstico 24 horas
- Tabla detallada de errores



