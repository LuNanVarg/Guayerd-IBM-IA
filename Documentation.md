# ETL y EDA Avanzada

Propósito: 
Realizar un proceso ETL (Extracción, Transformación y Carga) completo y aplicar Feature Engineering para unificar y enriquecer la data transaccional de la Tienda Aurelion, creando una base robusta para la Segmentación de Valor de Cliente (RFM) y el análisis de rentabilidad en la fase de Power BI.

Objetivos: 
1. Garantizar la calidad y consistencia del 100% de los datos transaccionales.

2. Implementar la Recategorización Avanzada de productos.

3. Integrar Métricas RFM para la identificación del segmento VIP.

4. Generar un Análisis Exploratorio de Datos (EDA) Avanzado que cubra las dimensiones de Cliente, Producto y Tendencias.

2. 🧹 Proceso ETL y Limpieza de Datos

Esta fase asegura la coherencia de los datos transaccionales.

    Unificación de Data: Se realizó una secuencia de 4 merge (uniones) utilizando la librería pandas (Detalle de Ventas ➡️ Ventas ➡️ Productos ➡️ Clientes) para crear un único dataset a nivel de línea de detalle.

    Estandarización y Consistencia: Se aplicó limpieza a las columnas categóricas (ej. nombre_cliente, ciudad, medio_pago) mediante normalización de texto (.str.strip(), .str.title(), .str.lower()).

    Recategorización Avanzada: Se implementó una lógica de corrección en la columna de categorías. Esto fue fundamental para corregir inconsistencias donde productos de consumo (ej. Bebidas) estaban clasificados incorrectamente como "Limpieza", creando la columna limpia y validada categoria_final.

3. 💡 Feature Engineering & Integración de Métricas

Esta es la sección que justifica la robustez del entregable, validando la integración de datos de alto valor.

El dataset consolidado fue enriquecido mediante la fusión de dos fuentes externas de KPIs, utilizando claves primarias (id_cliente, nombre_producto):

    Métricas de Cliente (RFM): Se integraron variables fundamentales para la segmentación, renombradas para evitar conflictos: importe_total_cliente (Valor Monetario), total_compras_cliente (Frecuencia), y ticket_promedio_cliente (Ticket Promedio).

    Métricas de Producto: Se incorporaron indicadores de rendimiento de producto como total_unidades_vendidas e importe_total_producto.

    Validación de Data: Se aplicó una conversión a tipo datetime a las columnas de fecha (fecha_venta, fecha_alta) para permitir el análisis temporal.

. 📊 Análisis Exploratorio de Datos (EDA) Avanzado

El análisis se centró en descubrir patrones de valor y segmentación utilizando una alta variedad de gráficos (Barra, Dispersión, Torta, Box Plot, Violin Plot, Heatmap, Histograma).

4.1 Análisis de Clientes y Segmentación (RFM)
Scatter Plot (Gasto vs. Ticket):
El gráfico de dispersión, dimensionado por frecuencia, muestra la segmentación de clientes. La concentración de puntos en la esquina superior derecha representa el Segmento VIP (Alto Gasto, Alta Frecuencia), el principal motor de ingresos.

Heatmap Cliente vs. Categoría:
Confirma el patrón de gasto de los Top 10 clientes: su consumo está fuertemente anclado en la categoría Alimentos, siendo Limpieza un gasto complementario y de menor volumen para este segmento.

Top Clientes: 
La tabla de los Top 10 Clientes por importe_total_cliente identifica a los individuos clave para las estrategias de retención.

4.2 Análisis de Productos y Transaccional
Distribución por Categoría (Torta):
El Gráfico de Torta confirma el dominio de la categoría Alimentos sobre el importe total, validando la precisión de la recategorización.

Violin Plot:
El Violin Plot (densidad de unidades vendidas) para el Top 5 de productos indica si los productos de mayor volumen se venden por unidad o en bultos, lo cual es vital para la logística de inventario.

Box Plot Importe vs. Pago:
El Box Plot revela la distribución del valor del ticket por medio de pago. Generalmente, los medios de pago electrónicos (Tarjeta, Transferencia) están asociados a los outliers de mayor importe.

Histograma/Línea de Tendencia:
El Histograma confirma que la mayoría de las transacciones son de bajo valor, con una fuerte asimetría positiva. El Gráfico de Línea (Tendencia Mensual) muestra la evolución de las ventas en el tiempo, identificando picos y valles estacionales.

5. 💡 Conclusiones y Oportunidades de Negocio:
El resultado final es un entregable de alto nivel técnico que sienta las bases para la estrategia de negocio.

Conclusión: Se logró un dataset completamente limpio y la integración del Feature Engineering (Métricas RFM) fue exitosa, permitiendo una segmentación de clientes clara y precisa. Todos los gráficos de la Sección 6 (EDA Avanzado) utilizan métricas validadas.

Oportunidad de Negocio Principal: Implementar una estrategia de venta cruzada y bundles dirigida a los clientes VIP (segmento de Alto Gasto) para incentivar la compra de productos de Limpieza y así diversificar sus patrones de consumo fuera de la categoría dominante (Alimentos).

Próximo Paso: El dataset enriquecido y segmentado está listo para ser exportado a Power BI para la creación del Dashboard Interactivo.
