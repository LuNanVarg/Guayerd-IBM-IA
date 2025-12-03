# 🌟 Informe del Proyecto Aurelion

---

## 🟢 1. Preparación del Entorno y Archivos

### ✅ Pasos iniciales

* Crear carpeta `AurelionProyecto/`
* Colocar los archivos `.csv` dentro de `Aurelion/`
* Abrir carpeta en VS Code → **Add Folder to Workspace**
* Revisar estructura de datos de cada archivo
* Crear archivos `.py` y `.md` para modular y documentar el proyecto

💡 *Tip: Mantener los archivos originales intactos como respaldo.*

---

## 🟡 2. Tablas y Estructura de Datos

| Tabla          | Archivo              | Columnas | Registros | Observaciones                                         |
| -------------- | -------------------- | -------- | --------- | ----------------------------------------------------- |
| Clientes       | `clientes.csv`       | 5        | 100       | Revisar duplicados en `nombre_cliente` y `email`      |
| Productos      | `productos.csv`      | 4        | 100       | Verificar categoría y duplicados en `nombre_producto` |
| Ventas         | `ventas.csv`         | 6        | 120       | Clientes pueden tener varias ventas                   |
| Detalle_Ventas | `detalle_ventas.csv` | 6        | 343       | Cada venta puede tener varios productos               |

**Notas de validación:** fechas correctas, IDs positivos, precios > 0, integridad referencial.

---

## 🔵 3. Requisitos de Instalación

### 💻 Software

* Python ≥ 3.8
* Editor: VS Code o PyCharm

### 📦 Librerías

```bash
pip install pandas numpy openpyxl matplotlib seaborn
```

⚡ *Tip: Mantener las versiones indicadas para reproducibilidad.*

---

## 🟠 4. Estándares de Datos y Validaciones

| Concepto         | Estándar          |
| ---------------- | ----------------- |
| Fechas           | YYYY-MM-DD        |
| IDs              | Enteros positivos |
| Precios/Importes | 2 decimales       |
| Cantidad         | Enteros positivos |

**Validaciones Clave: (Centralizadas en el módulo `Limpiar_Datos.py`)**

* `fecha_alta < fecha de venta`
* `precio_unitario > 0`
* `importe = cantidad * precio_unitario`
* Integridad referencial de IDs (Clientes-Ventas, Productos-DetalleVentas)
* Evitar duplicados en emails y nombres de productos

✅ Esto garantiza KPIs confiables y análisis precisos.

---

## 🟣 5. Problema y Solución

### ❗ Problema

* No hay visión consolidada de ventas
* Difícil segmentación de clientes por comportamiento
* Información por ciudad, categoría y medio de pago dispersa

### 💡 Solución

* Implementar el módulo `Limpiar_Datos.py` para integrar todas las tablas en un DataFrame consolidado.
* Limpiar y validar datos de forma estandarizada.
* Generar reportes y KPIs: ventas, clientes, ingresos, top 5 clientes.
* Identificar clientes sin compras recientes.

---

## 🟤 6. KPIs Principales

* Clientes totales, activos e inactivos
* Ventas totales y ticket promedio
* Ingresos por categoría, medio de pago y ciudad
* Top 5 clientes por monto total

📊 Todos los KPIs se calculan a partir del DataFrame consolidado.

---

## 🔴 7. Diagrama de Flujo del Proceso

```
[Inicio] 
   │
   ▼
[Cargar archivos CSV en DataFrames]
   │
   ▼
[EDA: inspección de columnas, tipos, nulos]
   │
   ▼
[LLAMADA al módulo Limpiar_Datos.py (ETL)]
   ├─ Conversión de tipos y Formatos
   ├─ Integración (Merge de las 4 talbas)
   └─ Validación de integridad referencial
   │
   ▼
[Generar DataFrame Consolidado (Limpio)]
   │
   ▼
[Calcular KPIs y generar reportes]
   │
   ▼
[Exportar: CSV y consola]
   │
   ▼
[Fin]
```

---

## ⚡ 8. Pseudocódigo Resumido

```
INICIO_PROGRAMA

// Cargar datos
df_clientes = CARGAR_CSV("clientes.csv")
df_productos = CARGAR_CSV("productos.csv")
df_ventas = CARGAR_CSV("ventas.csv")
df_detalle_ventas = CARGAR_CSV("detalle_ventas.csv")

// Respaldo de datos originales
COPIAR(df_clientes, df_productos, df_ventas, df_detalle_ventas)

// EDA
INSPECCIONAR(df_clientes, df_productos, df_ventas, df_detalle_ventas)

// Limpieza, Validación e Integración (Módulo Limpiar_Datos.py)
// La función Limpiar_Datos() maneja toda la lógica interna (tipos, validaciones, merges).
df_consolidado = LLAMAR_FUNCION(Limpiar_Datos, df_clientes, df_productos, df_ventas, df_detalle_ventas)

// KPIs
CALCULAR_CLIENTES_ACTIVOS_INACTIVOS(df_consolidado)
CALCULAR_TOTAL_VENTAS_INGRESOS_TICKET(df_consolidado)
GENERAR_REPORTES(df_consolidado)

// Exportación
GUARDAR_CSV(df_consolidado, "ventas_completo_LIMPIO.csv")

FIN_PROGRAMA
```

---

## 📌 9. Notas Finales

* Mantener los datos originales intactos
* Revisar las validaciones antes de generar análisis
* Actualizar este documento si se agregan nuevas tablas o KPIs

---

### 💬 Créditos

📌 **Autora:** Nancy Vargas
🎓 **Curso:** Fundamentos de Inteligencia Artificial – Guayerd & IBM SkillsBuild
📅 **Año:** 2025
💻 **Lenguaje:** Python 3.x
📚 **Temática:** Integración y análisis de datos de ventas

---

