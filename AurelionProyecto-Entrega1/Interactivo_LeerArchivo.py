# --------------------------------------------------------------------------------
#   AurelionProyecto ==> Interactivo_LeerArchivo.py
# -------------------------------------------------------------------------------
#  Script interactivo para explorar, LIMPIAR y combinar CSV del proyecto Aurelion
# --------------------------------------------------------------------------------

import pandas as pd
import os
import numpy as np 

# ---------------------------\
# Definir la ruta base
# ---------------------------
# (Mantener la ruta que uses en tu PC)
ruta_base = r"C:\Users\Luna\Desktop\Guayerd\AurelionProyecto\Aurelion"

if not os.path.exists(ruta_base):
    print(f"❌ La carpeta '{ruta_base}' no existe.")
    exit()

# ---------------------------------------------------------------------------
# Funciones de utilidad (listar_csv, leer_csv, mostrar_preview, guardar_csv)
# ---------------------------------------------------------------------------

def listar_csv():
    """ Lista archivos CSV en la carpeta """
    csvs = [f for f in os.listdir(ruta_base) if f.endswith(".csv")]
    if not csvs:
        print("⚠️ No hay archivos CSV disponibles.")
    else:
        print("\n📁 Archivos CSV disponibles:")
        for i, f in enumerate(csvs, 1):
            print(f"  {i}. {f}")
    return csvs

def leer_csv(nombre_archivo):
    """ Lee un CSV y devuelve DataFrame """
    ruta = os.path.join(ruta_base, nombre_archivo)
    if not os.path.exists(ruta):
        print(f"❌ Archivo no encontrado: {nombre_archivo}")
        return pd.DataFrame()
    try:
        df = pd.read_csv(ruta)
        if df.empty:
            print(f"⚠️ El archivo '{nombre_archivo}' está vacío.")
        return df
    except Exception as e:
        print(f"❌ Error al leer '{nombre_archivo}': {e}")
        return pd.DataFrame()

def mostrar_preview(df, nombre):
    """ Muestra las primeras filas de un DataFrame """
    print(f"\n👀 Preview de {nombre}:")
    if df.empty:
        print("  (Sin datos)")
    else:
        print(df.head())

def guardar_csv(df, nombre_archivo):
    """ Guarda un DataFrame en CSV """
    if df.empty:
        print(f"⚠️ No hay datos para guardar en '{nombre_archivo}'.")
        return
    ruta = os.path.join(ruta_base, nombre_archivo)
    df.to_csv(ruta, index=False)
    print(f"\n✅ Archivo guardado: {ruta}")

# ---------------------------------------------------------------------------
# Función para combinar y limpiar DataFrames 
# ---------------------------------------------------------------------------


def ventas_completo_LIMPIO(clientes_df, productos_df, ventas_df, detalle_ventas_df):
    """
    Combina los cuatro DataFrames (ventas, detalle_ventas, productos, clientes)
    para crear el informe completo de ventas.
    """
    
    print("\n⏳ Iniciando combinación de DataFrames (Merge)...")
    
    # 1. Unir Detalle_Ventas con Ventas (a nivel de transacción)
    df_merged = pd.merge(detalle_ventas_df, ventas_df, 
                         on='id_venta', how='left', suffixes=('_detalle', '_venta'))

    # 2. Unir con Productos (para obtener descripción y precio)
    df_merged = pd.merge(df_merged, productos_df, 
                         on='id_producto', how='left', suffixes=('', '_prod'))

    # 3. Unir con Clientes (para obtener datos del comprador)
    df_merged = pd.merge(df_merged, clientes_df, 
                         on='id_cliente', how='left', suffixes=('', '_cli'))
    
    # --- Pequeña limpieza/cálculo ---
    
    # **CORRECCIÓN CLAVE:** Solo renombramos la fecha. 
    # Usaremos la columna 'precio_unitario' que ya existe después de los merges.
    df_merged = df_merged.rename(columns={'fecha_venta': 'fecha'})
    
    # Calcular el total de la línea de venta, usando la columna correcta.
    # El archivo subido confirma que la columna se llama 'precio_unitario'.
    df_merged['total_linea'] = df_merged['precio_unitario'] * df_merged['cantidad']
    
    print("✅ Combinación completada. DataFrame listo.")
    return df_merged


# -----------------------------------
# Variables globales para DataFrames
# -----------------------------------
clientes = pd.DataFrame()
productos = pd.DataFrame()
ventas = pd.DataFrame()
detalle_ventas = pd.DataFrame()
clientes_ventas = pd.DataFrame()
ventas_completo = pd.DataFrame()

# ---------------------------
# Función principal del menú
# ---------------------------
def menu():
    global clientes, productos, ventas, detalle_ventas, clientes_ventas, ventas_completo

    while True:
        print("\n" + "="*60)
        print(" 🚀 EXPLORADOR INTERACTIVO DE CSV - AURELION ")
        print("="*60)
        print("[1] Listar archivos CSV disponibles")
        print("[2] Ver preview de un archivo CSV")
        print("[3] Combinar Clientes + Ventas (Merge Simple)")
        print("[4] Combinar y LIMPIAR DataFrames (Informe Completo)")
        print("[5] Guardar archivos combinados")
        print("[0] Salir")
        print("-"*60)

        opcion = input("Seleccioná una opción: ").strip()

        if opcion == "0":
            print("\n¡Hasta luego! 👋")
            break

        elif opcion == "1":
            listar_csv()

        elif opcion == "2":
            csvs = listar_csv()
            if csvs:
                try:
                    num = int(input("Número del archivo a mostrar: ").strip())
                    archivo = csvs[num-1]
                    df = leer_csv(archivo)
                    mostrar_preview(df, archivo)
                except (ValueError, IndexError):
                    print("Número inválido.")

        elif opcion == "3":
            # Leer archivos necesarios
            clientes = leer_csv("clientes.csv")
            ventas = leer_csv("ventas.csv")
            if not clientes.empty and not ventas.empty:
                clientes_ventas = pd.merge(ventas, clientes, on="id_cliente", how="left")
                mostrar_preview(clientes_ventas, "Clientes + Ventas")
            else:
                print("⚠️ No se puede combinar clientes y ventas.")

        elif opcion == "4":
            print("\n--- INICIANDO PROCESO ETL COMPLETO ---")
            # Leer archivos necesarios
            clientes = leer_csv("clientes.csv")
            productos = leer_csv("productos.csv")
            ventas = leer_csv("ventas.csv")
            detalle_ventas = leer_csv("detalle_ventas.csv")

            # LLAMADA A LA FUNCIÓN DE LIMPIEZA Y MERGE CON INTEGRIDAD (IMPORTADA)
            if not clientes.empty and not productos.empty and not ventas.empty and not detalle_ventas.empty:
                ventas_completo = ventas_completo_LIMPIO(clientes, productos, ventas, detalle_ventas) 
                
                # Mostrar el resultado
                mostrar_preview(ventas_completo, "Informe completo (Limpio y Consolidado)")
            else:
                print("⚠️ No se puede generar informe completo: faltan uno o más archivos base.")

        elif opcion == "5":
            if not clientes_ventas.empty:
                guardar_csv(clientes_ventas, "clientes_ventas.csv")
            if not ventas_completo.empty:
                guardar_csv(ventas_completo, "ventas_completo_LIMPIO.csv") # Se añade _LIMPIO para distinguirlo
            if clientes_ventas.empty and ventas_completo.empty:
                print("⚠️ No hay archivos combinados para guardar.")

        else:
            print("Opción inválida. Intentá de nuevo.")

# ---------------------------
# Ejecutar menú
# ---------------------------
if __name__ == "__main__":
    menu()

# ------------------------------------------------------------------------------------------------------------------------
# Para ejecutar este script, asegurarse de estar en la ruta correcta, agregar las lineas por orden dentro de la Terminal:
# C:\Users\Luna\Desktop\Guayerd\AurelionProyecto
# python Interactivo_LeerArchivo.py
# -------------------------------------------------------------------------------------------------------------------------