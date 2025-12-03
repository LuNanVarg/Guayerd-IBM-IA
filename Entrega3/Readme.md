# 🧭 PROYECTO AURELION - Entrega 3 (Modelo Predictivo)
## 🎯 Enfoque Individual: Regresión Lineal Múltiple

---

### 🔖 Badges

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikit-learn)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Regresion](https://img.shields.io/badge/Modelo-Regresión%20Lineal-005C99)
![Métricas](https://img.shields.io/badge/Métricas-R²%20y%20MAPE-E54A41)
![EDA](https://img.shields.io/badge/Data%20Analysis-EDA-00BFA6)

---

### 📘 Descripción General

El **Entrega 3** (Sprint 3) marca la transición del Análisis Exploratorio de Datos (EDA) al **Modelado Predictivo**. El foco es desarrollar una herramienta de Machine Learning que permita a la Tienda Aurelion **predecir el valor económico de cada venta**.

**Modelo Individual:** Se implementó un modelo de **Regresión Lineal Múltiple** para predecir la variable objetivo `importe`. Este enfoque prioriza la **interpretabilidad de los coeficientes** para identificar los factores que más impulsan el gasto.

**Resultados Clave:**
* **Capacidad Explicativa (R²):** El modelo explica el $\approx 83.33\%$ de la variabilidad del `importe`.
* **Impulsor Principal:** La **`cantidad`** vendida es el factor con el mayor impacto cuantificable en el importe final.

---

### 🧩 Estructura del Entrega 3

```
Entrega3_Aurelion/
│
├── README.md # Este archivo (Entrega3)
├── Entrega3_Docuemntacion.md  # Documentación técnica completa (ML + Interpretación)
├── Entrega_3.py  # Script ejecutable del modelo final (modularidad)
├── Entrega3ML.ipynb  # Notebook con código de Regresión, Métricas y Gráficos
└── consolidado.csv  # Dataset de entrada (Salida del Sprint 2)
```

---

### ⚙️ Requisitos y Dependencias

Para ejecutar y reproducir el modelo necesitás tener instalados:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
pip install jupyter
```
---

### 🚀 Cómo Ejecutar el Proyecto
📓 **Modo Notebook (Análisis y Gráficos - Recomendado)**
1. Abrí el archivo: Entrega3ML.ipynb.
2. Ejecutá las celdas en orden. El notebook realizará el preprocesamiento, entrenará el modelo y generará las métricas y visualizaciones.

**Modo Script (Validación de Modularidad)**
1. Abrí la terminal en el directorio del proyecto.
2. Ejecutá el script final:
3. Ejecutá las celdas en orden para reproducir:
* ETL
* Feature Engineering
* EDA
* Exportación del dataset final

---

### 🔄 Metodología Aplicada
🧹 Proceso ETL 
* Integración mediante 4 merges.
* Limpieza y estandarización de texto.
* Conversión de columnas de fecha a `datetime`.
* Exportación del dataset consolidado: `consolidado.csv`

### ✨ Feature Engineering
🧽 Recategorización Avanzada: creación de `categoria_final`
* Métricas RFM
* Métricas de producto
* Exportación del dataset enriquecido (`aurelion_consolidado_final.csv`)

---

### 📊 Análisis Exploratorio de Datos (EDA)
Se generaron visualizaciones clave:
* Gráficos de barras
* Pie Chart
* Scatter Plot
* Box Plot
* Violin Plot
* Heatmap
* Histogramas
* Tendencias temporales

### 🧠 Hallazgos Principales
```
| Área                 | Insight                                     | Visualización |
| -------------------- | ------------------------------------------- | ------------- |
| Segmentación Cliente | Clientes VIP claramente identificados       | Scatter       |
| Categorías           | Alimentos domina el ingreso                 | Pie / Box     |
| Patrones de Consumo  | Oportunidad de venta cruzada                | Heatmap       |
| Productos            | Diferencia entre venta por unidad o bulto   | Violin        |

```
---

### 📊 Alcance
* Dataset limpio y consolidado
* Variables enriquecidas (RFM + producto)
* Visualizaciones analíticas

---

### 🧱 Modelo del Proceso
* ETL → Limpieza → Recategorización → Métricas → Dataset Final
* Relaciones entre tablas validadas mediante merges
* Dataset final listo para análisis estratégico

---

## 💬 Créditos
```
Autora: Nancy Vargas
Curso: Fundamentos de Inteligencia Artificial — Guayerd & IBM SkillsBuild
Año: 2025
💻 Lenguaje: Python 3.
📚 Temática: Entrega2: ETL + Feature Engineering + EDA
🎨 Formatos: CLI + Jupyter Notebook

```
----
