# 📘 Documentación del Proyecto — ETL, Feature Engineering y EDA Avanzado (Entrega2)

### 🎯 Propósito General

El objetivo de este sprint fue construir un **dataset consolidado, limpio y enriquecido**, integrando las fuentes transaccionales de la Tienda Aurelion y aplicando Feature Engineering para habilitar análisis estratégicos como la Segmentación RFM y la rentabilidad por producto.  
Este dataset constituye la base para el Dashboard Interactivo en Power BI.

---

### 1. 🧹 Proceso ETL y Limpieza de Datos

La fase ETL garantizó la **calidad, coherencia y completitud** de todas las fuentes transaccionales.

### 🔗 1.1 Unificación de Data  
Se realizó una secuencia de *4 merges* utilizando pandas:

1. Detalle de Ventas  
2. Ventas  
3. Productos  
4. Clientes  

El resultado fue un **dataset transaccional a nivel de línea de detalle**, almacenado como `consolidado.csv`.

### ✔️ 1.2 Estandarización y Consistencia

Se aplicaron transformaciones para asegurar uniformidad:

- Normalización de texto: `.str.strip()`, `.str.title()`, `.str.lower()`
- Corrección y estandarización de columnas como `nombre_cliente`, `ciudad`, `medio_pago`
- Conversión a *datetime* en `fecha_venta` y `fecha_alta`

### 🧽 1.3 Recategorización Avanzada de Productos  
Se corrigieron inconsistencias donde productos de consumo (ej. Bebidas) estaban clasificados como “Limpieza”.  
Se generó la columna validada: **`categoria_final`**.

---

### 2. ✨ Feature Engineering e Integración de Métricas

El dataset fue enriquecido mediante la integración de métricas externas provenientes de:

- **metricas_cliente.csv**
- **metricas_producto.csv**

### 👤 2.1 Métricas de Cliente (RFM)

Se incorporaron y renombraron para evitar conflictos:

- `importe_total_cliente` (Monetario)
- `total_compras_cliente` (Frecuencia)
- `ticket_promedio_cliente` (Ticket Promedio)

Estas variables habilitan la segmentación de valor, destacando el **Segmento VIP**.

### 📦 2.2 Métricas de Producto  
Se integraron:

- `total_unidades_vendidas`
- `importe_total_producto`

Estas métricas permiten identificar top sellers y analizar la rentabilidad por categoría.

---

### 3. 📊 EDA Avanzado

El análisis exploró tres dimensiones principales: **Cliente**, **Producto** y **Tendencias**.  
Los gráficos desarrollados incluyen: Barras, Dispersión, Torta, Box Plot, Violin Plot, Heatmap e Histogramas.

---

### 3.1 Análisis de Clientes y Segmentación

#### 🔵 Scatter Plot (Gasto vs. Ticket Promedio)  
Permite identificar el **Segmento VIP**: clientes con alta frecuencia y alto gasto.

#### 🔥 Heatmap Cliente vs. Categoría  
Los Top 10 clientes concentran su gasto principalmente en **Alimentos**, mostrando oportunidad para Venta Cruzada con Limpieza.

#### 🏆 Ranking Top Clientes  
La tabla identifica a los clientes de mayor valor monetario.

---

### 3.2 Análisis de Productos

#### 🥧 Gráfico de Torta — Distribución por Categoría  
Confirmación: **Alimentos domina el ingreso total**.

#### 🎻 Violin Plot — Unidades Vendidas  
Ayuda a entender si los productos top se venden por unidad o en bultos.

#### 📦 Box Plot — Importe por Medio de Pago  
Los medios electrónicos muestran los outliers de mayor importe.

---

### 3.3 Tendencias Temporales  
El histograma confirma transacciones de bajo valor como mayoría.  
La línea de tendencia muestra picos y estacionalidad de ventas.

---

### 4. 💡 Conclusiones

### ✔️ Conclusión Final 
La estructura, el detalle de la sección Feature Engineering, y la descripción de los insights de los gráficos más complejos (Scatter Plot y Heatmap) son de alta calidad. Tu documentación es un entregable de nivel profesional.

### 🚀 Oportunidad Estratégica  
Aplicar **venta cruzada y bundles** al segmento VIP, incentivando compras fuera de Alimentos (principalmente hacia Limpieza).

---

