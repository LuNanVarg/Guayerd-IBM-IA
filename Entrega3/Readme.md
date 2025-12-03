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

### 📊 Modelo y Hallazgos Principales
```
| Métrica    | Valor           | Rol en el Negocio                                   |
| ---------- | --------------- | --------------------------------------------------- |
| R²         | 0.8333          | Capacidad explicativa (Alto rendimiento).           |
| MAPE       | 46.34%          | Error promedio porcentual de la predicción.         |
| Impulsor 1 | cantidad        | Factor de mayor impacto positivo en el gasto final. |
| Impulsor 2 | precio_unitario | Segundo factor de mayor impacto.                    |

```
---

### 🧠 Interpretación (Coeficientes)
El análisis de coeficientes lineal confirma que el volumen de la compra (cantidad) es el determinante más importante del importe de venta, siendo ≈2554 unidades monetarias más influyente que cualquier otra variable por unidad. El modelo permite cuantificar el impacto de los medios de pago (qr, tarjeta) y las categorías (Limpieza) en la generación de ingresos.

---

## 💬 Créditos
```
Autora: Nancy Vargas
Curso: Fundamentos de Inteligencia Artificial — Guayerd & IBM SkillsBuild
Año: 2025
💻 Lenguaje: Python 3.
📚 Temática: Entrega 3: Regresión Lineal Múltiple.
```
----
