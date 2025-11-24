# 🧭 PROYECTO AURELION - SPRINT 2 
## ETL Feature Engineering y Análisis Exploratorio de Datos (EDA)

---

## 🔖 Badges

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-ETL-150458?logo=pandas)
![Numpy](https://img.shields.io/badge/Numpy-Processing-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualización-11557C?logo=matplotlib)
![Seaborn](https://img.shields.io/badge/Seaborn-EDA-4C72B0?logo=python)
![ETL](https://img.shields.io/badge/ETL-Workflow-6A5ACD)
![Data%20Analysis](https://img.shields.io/badge/Data%20Analysis-EDA-00BFA6)

---

## 📘 Descripción General

El **Sprint 2** del Proyecto Aurelion continúa el trabajo iniciado en la Entrega 1, avanzando hacia la creación de un **Dataset Consolidado y Enriquecido** a partir de múltiples fuentes transaccionales.  

En esta fase se desarrolló:

- Un proceso **ETL completo** (extracción, transformación y carga).  
- Un **Feature Engineering avanzado**, incorporando métricas RFM y métricas de producto.  
- Un **Análisis Exploratorio de Datos (EDA)** con visualizaciones para entender patrones, segmentación y comportamiento de compras.  

Este sprint deja preparado el dataset final para su uso en **Power BI** o **Machine learning** y para el análisis estratégico del negocio.

---

## 🧩 Estructura del Sprint 2


Sprint2_Aurelion/
│
├── README.md # Este archivo (Sprint 2)
├── Documentation.md  # Documentación técnica del ETL y EDA
│
├── Entrega_2_ETL_EDA_Final.ipynb  # Notebook completo con ETL + Feature Engineering + EDA
│
├── consolidado.csv  # Dataset unificado previo al enriquecimiento
├── metricas_cliente.csv  # Métricas RFM por cliente
├── metricas_producto.csv  # Métricas por producto
│
└── aurelion_consolidado_final.csv  # Dataset final enriquecido (df_final)

---

## ⚙️ Requisitos Previos

Para ejecutar el ETL y el EDA necesitás tener instalados:

```bash
pip install pandas numpy matplotlib seaborn openpyxl
pip install jupyter

```
---

## 🚀 Cómo Ejecutar el Proyecto
📓 1. Modo Notebook (Recomendado)

1. Abrí Jupyter Notebook o JupyterLab.
2. Cargá el archivo:

       Entrega_2_ETL_EDA_Final.ipynb

3. Ejecutá las celdas en orden para reproducir:
* ETL
* Feature Engineering
* EDA
* Exportación del dataset final

---

🔄 Metodología Aplicada
🧹 Proceso ETL 
* Integración mediante 4 merges.
* Limpieza y estandarización de texto.
* Conversión de columnas de fecha a `datetime`.
* Exportación del dataset consolidado: `consolidado.csv`

✨ Feature Engineering
🧽 Recategorización Avanzada: creación de `categoria_final`
* Métricas RFM
* Métricas de producto
* Exportación del dataset enriquecido (`aurelion_consolidado_final.csv`)

---

📊 Análisis Exploratorio de Datos (EDA)
Se generaron visualizaciones clave:
* Gráficos de barras
* Pie Chart
* Scatter Plot
* Box Plot
* Violin Plot
* Heatmap
* Histogramas
* Tendencias temporales

🧠 Hallazgos Principales
```
| Área                 | Insight                                     | Visualización |
| -------------------- | ------------------------------------------- | ------------- |
| Segmentación Cliente | Clientes VIP claramente identificados       | Scatter       |
| Categorías           | Alimentos domina el ingreso                 | Pie / Box     |
| Patrones de Consumo  | Oportunidad de venta cruzada                | Heatmap       |
| Productos            | Diferencia entre venta por unidad o bulto   | Violin        |

```
---

## 📊 Alcance
* Dataset limpio y consolidado
* Variables enriquecidas (RFM + producto)
* Visualizaciones analíticas

---

## 🧱 Modelo del Proceso
* ETL → Limpieza → Recategorización → Métricas → Dataset Final
* Relaciones entre tablas validadas mediante merges
* Dataset final listo para análisis estratégico

---

## 💬 Créditos

Autora: Nancy Vargas
Curso: Fundamentos de Inteligencia Artificial — Guayerd & IBM SkillsBuild
Año: 2025
Sprint 2: ETL + Feature Engineering + EDA

