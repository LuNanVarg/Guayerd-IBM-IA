# -------------------------------------------------------
#   AurelionProyecto ==> Limpiar_Datos.py
# -------------------------------------------------------
#  Módulo que contiene la función de Limpieza, Transformación y Validación
#  para los datos de Aurelion. Este script NO es interactivo; es una LIBRERÍA
#  de funciones para ser importada.
# -------------------------------------------------------

import pandas as pd
import numpy as np # Necesario para algunas validaciones

def Limpiar_Datos(df_clientes, df_productos, df_ventas, df_detalle_ventas):
    """
    Realiza la limpieza (tipos de datos, formatos), unión (merge)
    y una VALIDACIÓN DE INTEGRIDAD REFERENCIAL clave para el Proyecto Aurelion.
    
    Args:
        df_clientes (pd.DataFrame): Datos de clientes.
        df_productos (pd.DataFrame): Datos de productos.
        df_ventas (pd.DataFrame): Datos de ventas principales.
        df_detalle_ventas (pd.DataFrame): Datos de detalle de cada producto en una venta.
        
    Returns:
        pd.DataFrame: DataFrame final consolidado y limpio (df_consolidado).
    """
    print("\n--- 🧹 FASE DE LIMPIEZA Y TRANSFORMACIÓN ---")
    
    # 1. CONVERSIÓN DE TIPOS Y RECALCULO DE IMPORTE
    
    # Convertir Fechas a tipo datetime 
    df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'], errors='coerce')
    df_clientes['fecha_alta'] = pd.to_datetime(df_clientes['fecha_alta'], errors='coerce')

    # Limpieza de valores numéricos en detalle_ventas 
    columnas_numericas = ['cantidad', 'precio_unitario', 'importe']
    for col in columnas_numericas:
        if col in df_detalle_ventas.columns:
            # Eliminar comas o signos monetarios y convertir a float
            df_detalle_ventas[col] = df_detalle_ventas[col].astype(str).str.replace(r'[$,]', '', regex=True)
            df_detalle_ventas[col] = pd.to_numeric(df_detalle_ventas[col], errors='coerce')

    # Recalcular importe_calculado para validación
    df_detalle_ventas['importe_calculado'] = df_detalle_ventas['cantidad'] * df_detalle_ventas['precio_unitario']
    print("✅ Tipos de datos convertidos. Importes recalculados para validación.")

    # 2. UNIÓN DE DATOS (MERGE)
    print("\n--- 🔗 FASE DE INTEGRACIÓN (MERGE) ---")
    
    # Paso 1: Detalle_Ventas con Productos
    df_consolidado = pd.merge(
        df_detalle_ventas, 
        df_productos[['id_producto', 'categoria']], 
        on='id_producto', 
        how='left'
    )
    
    # Paso 2: Resultado con Ventas
    df_consolidado = pd.merge(
        df_consolidado, 
        df_ventas[['id_venta', 'fecha', 'id_cliente', 'medio_pago']], 
        on='id_venta', 
        how='left'
    )
    
    # Paso 3: Resultado con Clientes
    df_consolidado = pd.merge(
        df_consolidado, 
        df_clientes[['id_cliente', 'ciudad', 'fecha_alta']], 
        on='id_cliente', 
        how='left'
    )
    
    # 3. VALIDACIÓN DE INTEGRIDAD REFERENCIAL POST-MERGE
    print("\n--- 🚧 VALIDACIÓN DE INTEGRIDAD REFERENCIAL ---")
    
    # Chequeo 1: Integridad Producto-Venta 
    productos_sin_match = df_consolidado['categoria'].isnull().sum()
    if productos_sin_match > 0:
        print(f"❌ Alerta: {productos_sin_match} registros de Venta no tienen un Producto asociado.")
    else:
        print("✅ Integridad Producto-Venta verificada correctamente.")

    # Chequeo 2: Integridad Cliente-Venta
    ventas_sin_cliente = df_consolidado['ciudad'].isnull().sum()
    if ventas_sin_cliente > 0:
        print(f"❌ Alerta: {ventas_sin_cliente} registros de Venta no tienen un Cliente asociado.")
    else:
        print("✅ Integridad Cliente-Venta verificada correctamente.")
        
    print(f"\n✅ DataFrames consolidados. Filas totales: {len(df_consolidado)}")
    
    return df_consolidado

