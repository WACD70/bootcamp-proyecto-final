# bootcamp-proyecto-final
Reposotorio para demostración de proyecto final de bootcamp python 2
#  Modelo Predictivo de Demanda Espaciotemporal de Taxis en Nueva York

Sistema inteligente que predice la demanda de taxis por zona y franja horaria en la ciudad de Nueva York, utilizando datos históricos y técnicas de *Machine Learning* para optimizar la distribución de unidades y reducir los tiempos de espera de los pasajeros.

---

##  BADGES

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-orange)
![ScikitLearn](https://img.shields.io/badge/Scikit--learn-ML%20Model-yellow)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow)

---

##  PROBLEMA QUE RESUELVE (El "Por qué")

La empresa de taxis de Nueva York enfrenta desequilibrios entre la oferta y la demanda de vehículos en distintas zonas y horarios.  
Actualmente, la planificación operativa se basa en la experiencia de los supervisores, lo que genera:

- Tiempos de espera prolongados para los clientes.  
- Exceso de taxis vacíos circulando sin pasajeros.  
- Pérdidas económicas por ineficiencia en la asignación de flota.  

Este proyecto busca **anticipar los picos de demanda** mediante un modelo predictivo, permitiendo una gestión proactiva que mejore la eficiencia y la satisfacción de los usuarios.

---

##  SOLUCIÓN PROPUESTA (El "Qué")

Se desarrolla un sistema de predicción de demanda que:
- Analiza patrones históricos de viajes, horarios y ubicación.  
- Integra variables temporales (hora, día, temporada) y geográficas.  
- Predice la cantidad esperada de viajes por zona y hora.  
- Muestra los resultados en un **dashboard interactivo** con mapas de calor y gráficos de tendencia.  
- Permite a los coordinadores de operaciones tomar decisiones informadas sobre la distribución de taxis.

**Outputs generados:**
- Predicciones de demanda por zona y franja horaria (en CSV o BD).  
- Visualizaciones de demanda estimada vs. real.  
- Reporte de métricas del modelo (MAE, RMSE, R²).

---

##  CARACTERÍSTICAS PRINCIPALES (Features)

-  Análisis temporal (hora, día, semana, temporada).  
-  Segmentación espacial de la ciudad mediante clustering geográfico.  
-  Entrenamiento de modelos de regresión y series de tiempo.  
-  Dashboard visual para la interpretación de resultados.  
-  Predicciones automáticas de demanda para distintos escenarios.  
-  Reporte con métricas de evaluación y recomendaciones.

---

##  TECNOLOGÍAS UTILIZADAS (Tech Stack)

**Lenguaje principal:**  
- Python 3.10+

**Librerías y frameworks:**  
- Pandas, NumPy (procesamiento y limpieza de datos)  
- Scikit-learn (modelado y evaluación de regresión)  
- XGBoost / Prophet / LSTM (predicción de demanda temporal)  
- Matplotlib, Seaborn (visualización de datos)  
- Streamlit o Power BI (dashboard interactivo)  

**Infraestructura y despliegue:**  
- PostgreSQL (almacenamiento de datos)  
- Flask (API REST, opcional)  
- Docker (entorno reproducible)  

---

##  Dataset utilizado

**Fuente:**  
[NYC Yellow Taxi Trip Data - Kaggle](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data)

**Volumen estimado:**  
5 a 10 millones de registros (muestra de un mes).

**Principales variables:**
- pickup_datetime, pickup_latitude, pickup_longitude  
- dropoff_latitude, dropoff_longitude  
- passenger_count, trip_distance, fare_amount  
- payment_type, temporal features (hora, día, semana)

---

##  Estado del proyecto
>  En desarrollo — primera versión del modelo y dashboard en construcción.

---

##  Licencia
Este proyecto se distribuye bajo la licencia **MIT**.  
Puedes usarlo, modificarlo y adaptarlo libremente con atribución.

---

##  Autor
**William Castillo**  
Proyecto académico — Ciencia de Datos Aplicada  
Basado en dataset público de la NYC Taxi & Limousine Commission

## Estructura del proyecto
bootcamp-proyecto-final/
├── data/                          # 📊 Datos del proyecto
│   ├── external/                  # Dataset descargado desde Kaggle
│   ├── interim/                   # Datos intermedios (procesamiento)
│   └── processed/                 # Datos limpios y listos para el modelo
│
├── docs/                          # 📚 Documentación y reportes
│   ├── data_dictionary.md
│   ├── model_card.md
│   └── project_charter.md
│
├── models/                        # 🤖 Modelos entrenados (.pkl)
│
├── notebooks/                     # 📓 Notebooks Jupyter (EDA)
│
├── reports/                       # 📈 Reportes y visualizaciones
│   └── figures/
│
├── src/                           # 💻 Código fuente
│   ├── data/
│   │   ├── clean_dataset.py
│   │   ├── make_dataset.py
│   │   └── nyc_taxi_demand_linear_timeseries.py
│   ├── features/
│   │   └── build_features.py
│   ├── models/
│   │   ├── train_model.py
│   │   └── predict_model.py
│   ├── visualization/
│   │   └── visualize.py
│   └── tests/
│       ├── test_data.py
│       └── test_models.py
│
├── requirements.txt               # 📦 Dependencias
├── setup.py                       # ⚙️ Instalación del proyecto
├── LICENSE                        # 📄 Licencia MIT
└── README.md                      # 📖 Este archivo

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/WACD70/bootcamp-proyecto-final.git
cd bootcamp-proyecto-final
```

### 2. Crear un entorno virtual (recomendado)
```bash
# En Linux/Mac
python -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar el pipeline completo
```bash
# 1. Limpiar y preparar los datos
python src/data/clean_dataset.py

# 2. Entrenar el modelo
python src/models/train_model.py

# 3. Generar predicciones
python src/models/predict_model.py

# 4. Crear visualizaciones
python src/visualization/visualize.py
```


## Resultado final

- El sistema genera:
- Predicciones en formato .csv o .pkl
- Gráficos de demanda por zona y hora
- Reporte con métricas del modelo (MAE, RMSE, R²)

## Autor
**WACD70**
- GitHub: [@WACD70](https://github.com/WACD70)