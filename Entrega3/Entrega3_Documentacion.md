# 🛒 **Introducción al Proyecto Tienda Aurelion**

## Índice de Contenidos

## **Sprint 1**
1. [Tema, problema y solución](#1-tema-problema-y-solución)  
2. [Dataset de referencia: resumen y definición](#2-dataset-de-referencia-resumen-y-definición)  
3. [Estructura por tabla: columnas, tipos y escalas](#3-estructura-por-tabla-columnas-tipo-y-escala-de-medición)  
4. [Escalas de medición: descripción y ejemplos](#4-escales-de-medición-descripción-y-ejemplos)  
5. [Sugerencias y mejoras con GitHub Copilot](#5-sugerencias-y-mejoras-con-copilot)  

---

## **Sprint 2**
6. [Estadísticas descriptivas básicas](#6-estadísticas-descriptivas-básicas)  
7. [Distribuciones de variables](#7-identificación-del-tipo-de-distribución-de-variables)  
8. [Correlaciones entre variables principales](#8-análisis-de-correlaciones-entre-variables-principales)  
9. [Detección de outliers](#9-detección-de-outliers)  
10. [Interpretación de resultados y limpieza final](#10-interpretación-de-resultados-y-limpieza-final)  

---

## **Sprint 3 — Modelo Individual (Regresión Múltiple)**
11. [Objetivo del modelo](#11-objetivo-del-modelo)  
12. [Algoritmo elegido y justificación](#12-algoritmo-elegido-y-justificado)  
13. [Entradas (X) y salida (y)](#13-entradas-x-y-salida-y)  
14. [Métricas de evaluación](#14-métricas-de-evaluación)  
15. [Modelo ML implementado](#15-modelo-ml-implementado)  
16. [División train/test y entrenamiento](#16-división-traintest-y-entrenamiento)  
17. [Predicciones y métricas calculadas](#17-predicciones-y-métricas-calculadas)  
18. [Resultados e interpretación de coeficientes](#18-resultados-e-interpretación-de-coeficientes)  

---

# 0. Introducción al Proyecto **Tienda Aurelion**

El **Proyecto Tienda Aurelion** busca analizar ventas y comportamiento de clientes mediante una solución completa basada en **Data Science y Machine Learning**.

La documentación recorre todas las etapas del proyecto: desde la organización y limpieza de datos hasta el entrenamiento y evaluación de un modelo predictivo.

---

# 1. Tema, problema y solución

## **1.1. Tema**
Análisis de ventas, clientes y productos en **Tienda Aurelion**.

## **1.2. Problema**
La tienda presenta dificultades para **organizar, analizar y aprovechar su información transaccional**.  
Esto causa:

- Falta de reportes confiables  
- Imposibilidad de identificar **patrones de compra**  
- Dificultad para optimizar **inventario, ventas y estrategias comerciales**

## **1.3. Solución**
Se propone un **sistema de análisis de datos** basado en:

- Procesamiento en **Python**  
- Base de datos estructurada y unificada  
- Limpieza y normalización de información  
- Modelado predictivo con **Machine Learning**  
- Integración futura con **Power BI** para dashboards interactivos  

### **Fases del proyecto (Sprints)**

- **Sprint 1:** Documentación y análisis inicial  
- **Sprint 2:** **ETL + EDA** (limpieza, unificación, exploración)  
- **Sprint 3:** Regresión Lineal Múltiple para predecir *importe de venta*  
- **Sprint 4:** En planificación  

---

## Sprint 3 - **DOCUMENTACIÓN INDIVIDUAL — MODELO DE REGRESIÓN DE VENTAS**

---

## 11. Objetivo del Modelo

El objetivo principal es predecir el **importe final de una venta** de la Tienda Aurelion.

Las variables de entrada (precio unitario, cantidad, categoría, ciudad, medio de pago) se utilizan para cuantificar el gasto esperado y entender el peso de cada factor.

**Tipo de problema:** Aprendizaje supervisado — *Regresión Lineal Múltiple*

---

## 12. Algoritmo Elegido y Justificación

### **Algoritmo:** `Regresión Lineal Múltiple`

### **Justificación**
 1. Naturaleza del Objetivo: El `importe` es un valor numérico continuo, ideal para los métodos de regresión.

2. Rendimiento Comprobado: El modelo simple explicaba solo ≈20% de la varianza. Con la inclusión de múltiples variables (Regresión Múltiple), el poder explicativo mejoró drásticamente a ≈84%.

3. Transparencia de Negocio: La Regresión Lineal ofrece coeficientes interpretables que explican el impacto directo y cuantificable (en pesos) de cada variable sobre la venta.

---

## 13. Entradas (X) y Salida (y)

### **Variables de entrada (X) - Features**  
- `precio_unitario`  
- `cantidad`  
- `categoria_corregida` (codificada)  
- `ciudad` (codificada)  
- `medio_pago` (codificada)  

### **Variable objetivo (y) - Target**  
- `importe` (Monto total de la venta)

---

## 14. Métricas de Evaluación
```
| Métrica  |        Descripción                                                 |        Foco                      |
|----------|------------------------------------------------------------------- |----------------------------------|
| **R²**   | Proporción de la varianza explicada por las features (0 a 1).      | Capacidad Explicativa            |
| **RMSE** | Raíz del Error Cuadrático Medio, en la escala original del importe.| Penalización de Errores Grandes  |
| **MAE**  | Error absoluto promedio, en pesos.                                 | Facilidad de Interpretación      |
| **MAPE** | Error Porcentual Medio (Diferenciador).                            | Métrica para Gestión de Negocio  |
```
---

## 15. Modelo ML Implementado

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
```
El modelo se construye a partir de la clase `LinearRegression` de la librería Scikit-learn, utilizando un enfoque que aplica One-Hot Encoding a las variables categóricas antes del entrenamiento.

---
## 16. División Train/Test y Entrenamiento
* **División**: Se utiliza la función `train_test_split` para separar el dataset limpio en 80% para entrenamiento y 20% para prueba `(test_size=0.2)`.

* **Propósito**: El conjunto de prueba se reserva para medir la capacidad del modelo de generalizar a datos no vistos y evitar el sobreajuste (overfitting).

---
## 17. Predicciones y Métricas Calculadas
Se realizaron predicciones sobre el 20% de los datos reservados para la prueba (`Test Set`). Los siguientes valores confirman el alto rendimiento y la validez del modelo de Regresión Lineal Múltiple:
```
| Métrica  | Valor Calculado |  Rol y Significado                                         |
| -------- | --------------- |----------------------------------------------------------- |
| **R²**   |   0.8333        | El modelo explica el ≈83.3% de la variabilidad del importe.|
| **RMSE** |   1694.48       | Desviación estándar del error en pesos.                    |
| **MAE**  |   1246.05       | Error absoluto promedio de las predicciones.               |
| **MAPE** |   46.34%        | Métrica clave de negocio. El error promedio de predicción. |
```

---
## 18. Resultados e Interpretación de Coeficientes

**A. Rendimiento Global del Modelo**
```
| Métrica  | Valor Calculado   |  Rol y Significado                                     |
| -------- | ----------------- |------------------------------------------------------- |
| R²       |    0.8333         | El modelo explica el ≈83.33% de la variabilidad del i. |
| MAE      |    1246.05        | En promedio, la predicción se desvía en ≈1246 pesos.   |
| RMSE     |    1694.48        | Desviación estándar del error en pesos.                |
| MAPE     |    46.34%         | El error de predicción promedio es del ≈46.34%         |

```

**B. Impulsores de Venta (Análisis de Coeficientes)**
```
| Variable                       | Valor Calculado |  Rol y Significado                                                                                        |
| ------------------------------ | --------------- | --------------------------------------------------------------------------------------------------------- |
| `cantidad`                     |    +2553.84     | Impulsor Primario: Por cada unidad adicional vendida, el importe aumenta en ≈2554 pesos.                  |
| `medio_pago_qr`                |    +426.45      | Una venta con QR resulta, en promedio, en ≈426 pesos más de importe, comparada con el medio de pago base. |
| `categoria_corregida_Limpieza` |    −379.39      | El importe de una venta de Limpieza es ≈379 pesos menor, en promedio, que la venta de Alimentos.          |
| `ciudad_Rio Cuarto`            |    −287.47      | Las ventas en Río Cuarto tienen un importe ≈287 pesos menor que las ventas de la ciudad base.             |
| `medio_pago_tarjeta`           |    +205.04      | Una venta con Tarjeta tiene un importe ≈205 pesos mayor que el pago base.                                 |

```

**C. Conclusión Global de la Regresión**

1. Capacidad Explicativa: El modelo es altamente predictivo, con un R2 de 0.8333. Esto significa que las features seleccionadas (cantidad, precio, medio de pago, etc.) explican la gran mayoría del comportamiento del gasto del cliente.

2. Foco de Negocio: El factor cantidad es, por amplio margen, el principal impulsor del importe. Esta información es crucial para diseñar estrategias de promoción enfocadas en el volumen (ej., descuentos por comprar la tercera unidad).

3. Gráfica Predicción vs. Real: La visualización confirma el excelente ajuste del modelo, ya que los puntos de predicción se agrupan firmemente alrededor de la línea ideal (y=x), validando la solidez de las métricas.