# 🧭 PROYECTO AURELION - SPRINT 2: ETL y Análisis Exploratorio de Datos

## 1. INTRODUCCIÓN

Este documento resume la metodología y los resultados clave obtenidos durante el Sprint 2 del Proyecto Aurelion, centrado en el pre-procesamiento, limpieza y enriquecimiento de los datos transaccionales. El objetivo principal fue crear un **Dataset Consolidado y Enriquecido** listo para el análisis estratégico y la visualización en Power BI.

## 2. METODOLOGÍA DEL SPRINT (ETL y Feature Engineering)

El Sprint 2 abordó la integración de los cuatro datasets fuente y el enriquecimiento de las variables para el Análisis de Valor de Cliente.

### 2.1 Proceso ETL (Extracción, Transformación y Carga)

* **Fuentes de Datos:** Se utilizaron cuatro archivos CSV/Excel: `clientes`, `productos`, `ventas` y `detalle_ventas`.
* **Unificación:** Se realizaron una secuencia de 4 operaciones `merge` (uniones) para consolidar la data transaccional a nivel de línea de detalle, resultando en el archivo `consolidado.csv`.
* **Limpieza:** Se aplicaron transformaciones de estandarización de texto (minúsculas, mayúsculas, eliminación de espacios) en columnas como `nombre_cliente` y `medio_pago`.

### 2.2 Feature Engineering y Recategorización Avanzada

* **Recategorización de Productos:** Se implementó una **Recategorización Avanzada** (columna `categoria_final`) para corregir inconsistencias (ej. productos de consumo clasificados como "Limpieza"), asegurando la coherencia del análisis por categoría.
* **Integración de Métricas RFM (Valor de Cliente):** Se enriqueció el dataset final fusionando métricas pre-calculadas (desde `metricas_cliente.csv`), incluyendo: **`importe_total_cliente`** y **`frecuencia_compra_cliente`**.
* **Output Final:** El resultado es un **Dataset Enriquecido** (`df_final` en el notebook) que contiene todas las variables transaccionales y de valor.

## 3. ANÁLISIS EXPLORATORIO DE DATOS (EDA) AVANZADO

El EDA se centró en la exploración del valor de cliente y la rentabilidad del producto, utilizando una variedad de gráficos (Barra, Scatter, Torta, Box Plot, Violin Plot y Heatmap).

| Área de Análisis | Visualización Clave | Hallazgo Estratégico |
| :--- | :--- | :--- |
| **Segmentación Cliente (RFM)** | Scatter Plot (Gasto vs. Ticket) | Identificación del **Segmento VIP** (Alto Gasto, Alta Frecuencia) como foco prioritario de retención y marketing. |
| **Rentabilidad de Categoría** | Pie Chart / Box Plot | Confirmación del **dominio de la categoría Alimentos** sobre el ingreso total. El Box Plot revela la dispersión del valor del ticket por `medio_pago`. |
| **Patrones de Gasto** | Heatmap Cliente vs. Categoría | Se observa la fuerte concentración del gasto de los clientes VIP en Alimentos, indicando una clara oportunidad de **Venta Cruzada** con productos de Limpieza. |
| **Inventario/Logística** | Violin Plot | Muestra la densidad de unidades vendidas por producto, ayudando a determinar si los productos de alto volumen se venden por unidad o en bultos. |

## 4. CONCLUSIONES Y PRÓXIMOS PASOS

### 4.1 Conclusiones del Sprint 2

El proyecto concluye con un dataset **robusto y validado**, listo para la etapa de visualización. La implementación del **Feature Engineering** y la **Recategorización Avanzada** permiten pasar de un análisis descriptivo básico a un análisis de segmentación y valor de negocio.

### 4.2 Próximos Pasos

1.  **Dashboarding (Power BI):** Exportar el dataset enriquecido (`df_final` / `aurelion_consolidado_final.csv`) para la creación de visualizaciones interactivas.
2.  **KPIs Estratégicos:** Centrar la visualización en la rentabilidad por segmento de clientes y la estacionalidad de las categorías.