# -------------------------------------------------------------
#   AurelionProyecto ==> ExploradorDoc.py
# -------------------------------------------------------------
#  Este script debe guardarse en:
#     /AurelionProyecto
#  Leerá los archivos .md (Markdown) que estén en esa carpeta.
# -------------------------------------------------------------

#Librerías usadas:
import os
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional

# ---------------------------
# Funciones utilitarias
# ---------------------------

def clear_screen() -> None:
    """ Limpia la pantalla del terminal """
    os.system('cls' if os.name == 'nt' else 'clear')  # cls = Windows / clear = Linux o Mac


def listar_archivos(carpeta: str, extension: Optional[str] = None) -> List[str]:
    """ Devuelve una lista de archivos en la carpeta dada que coincidan con la extensión. """

    # Verifica que la carpeta exista aantes de intentar leerla
    if not os.path.exists(carpeta):
        print(f"❌ No se encontró la carpeta '{carpeta}'")
        return []

    # Recorre los archivos dentro de la carpeta y filtra los que coincidan con la extensión (ejemplo: .md)
    archivos = [
        f for f in os.listdir(carpeta)
        if os.path.isfile(os.path.join(carpeta, f))
        and (not extension or f.lower().endswith(extension.lower()))
    ]
    # Si no hay archivos encontrados
    if not archivos:
        print(f"⚠️ No hay archivos con extensión '{extension or '*'}' en '{carpeta}'.")
        return []

    # Muestra la lista de archivos encontrados
    print(f"\n📂 Archivos encontrados en '{carpeta}':")
    for i, archivo in enumerate(archivos, 1):
        print(f"{i}. {archivo}")
    print()
    return archivos
2

# --------------------------------
# Funciones de lectura y parseo
# --------------------------------

def leer_archivo(ruta: str) -> Optional[str]:
    """ Lee un archivo Markdown (.md) con diferentes codificaciones posibles. """
    p = Path(ruta) # Convierte la ruta a un objeto Path 
    if not p.exists():
        print(f"❌ Error: No se encontró el archivo '{'/Informe.md'}'")
        return None

    # Intenta leer el archivo con varios encodings (por si hay caracteres especiales)
    for enc in ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']:
        try:
            with p.open('r', encoding=enc) as f:
                contenido = f.read()
                if contenido:
                    return contenido
        except (UnicodeDecodeError, UnicodeError):
            continue

    # Si ninguna codificación funcionó, intenta leer en binario e ignora errores
    try:
        with p.open('rb') as f:
            return f.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None

def extraer_secciones(contenido: str) -> List[Dict[str, Any]]:
    """ Extrae secciones del Markdown en secciones según los encabezados (#). """
    secciones: List[Dict[str, Any]] = []
    lineas = contenido.split('\n')
    seccion_actual = {'titulo': 'Inicio', 'nivel': 0, 'contenido': '', 'linea': 1}
    i = 0

    while i < len(lineas):
        linea = lineas[i]
        
        # Detecta título tipo Markdown: # Titulo, ## Subtítulo, etc. 
        match = re.match(r'^\s*(#{1,6})\s*(.+?)\s*$', linea)  # Detecta encabezados tipo "# Título"
        if match:
            # Si había una sección anterior, la guarda
            if seccion_actual['contenido'].strip() or seccion_actual['titulo'] != 'Inicio':
                secciones.append(seccion_actual)
                #Crea nueva sección con título y nivel 
            nivel = len(match.group(1))
            titulo = match.group(2).strip()
            seccion_actual = {'titulo': titulo, 'nivel': nivel, 'contenido': '', 'linea': i + 1}
            i += 1
            continue

        # Detecta encabezados subrayados (estilo antiguo Markdown)
        if i + 1 < len(lineas) and re.match(r'^\s*(=+|-+)\s*$', lineas[i + 1]):
            if seccion_actual['contenido'].strip() or seccion_actual['titulo'] != 'Inicio':
                secciones.append(seccion_actual)
            titulo = linea.strip()
            nivel = 1 if lineas[i + 1].startswith('=') else 2
            seccion_actual = {'titulo': titulo, 'nivel': nivel, 'contenido': '', 'linea': i + 1}
            i += 2
            continue

        # Si no es título, se suma como contenido.
        seccion_actual['contenido'] += linea + '\n'
        i += 1
 
    # Guarda la última sección del documento
    if seccion_actual['contenido'].strip() or seccion_actual['titulo'] != 'Inicio':
        secciones.append(seccion_actual)

    return secciones

# ---------------------------
# Funciones de visualización
# ---------------------------

def mostrar_menu_principal():
    """Muestra el menú principal en pantalla"""
    clear_screen()
    print("\n" + "="*60)
    print(" 🚀 EXPLORADOR DE DOCUMENTACIÓN PROYECTO AURELION ")
    print("="*60)
    print("\n[1] Ver índice de secciones")
    print("[2] Buscar contenido")
    print("[3] Ver sección específica")
    print("[4] Ver todo el documento")
    print("[5] Estadísticas del documento")
    print("[0] Salir")
    print("-"*60)

def mostrar_indice(secciones: List[Dict[str, Any]]):
    """Muestra el índice con las secciones detectadas"""
    print("\n🗂️  ÍNDICE DE SECCIONES\n" + "-"*50)
    for i, sec in enumerate(secciones, 1):
        indent = "  " * max(0, sec['nivel'] - 1)  # Indenta subtítulos
        print(f"{i}. {indent}{sec['titulo']}")
    print()

def mostrar_seccion(seccion: Dict[str, Any]):
    """Muestra una sección completa del documento"""
    print("\n" + "="*50)
    print(f"{'#' * seccion['nivel']} {seccion['titulo']}")
    print("="*50)
    print(f"Línea: {seccion['linea']}\n")
    print(seccion['contenido'].strip())
    print("\n" + "-"*50)

def buscar_en_contenido(secciones: List[Dict[str, Any]], termino: str) -> List[Any]:
    """Busca un término dentro del contenido y devuelve las secciones que lo contienen"""
    resultados = []
    for i, sec in enumerate(secciones, 1):
        if termino.lower() in (sec['titulo'] + sec['contenido']).lower():
            resultados.append((i, sec))
    return resultados

def mostrar_estadisticas(contenido: str, secciones: List[Dict[str, Any]]):
    """Muestra estadísticas del documento (líneas, palabras, caracteres, secciones)"""
    total_lineas = len(contenido.split('\n'))
    total_palabras = len(contenido.split())
    total_caracteres = len(contenido)
    print("\n📊 ESTADÍSTICAS")
    print("-"*40)
    print(f"Total de líneas: {total_lineas}")
    print(f"Total de palabras: {total_palabras}")
    print(f"Total de caracteres: {total_caracteres}")
    print(f"Total de secciones: {len(secciones)}")

# ---------------------------
# Ejecución interactiva (menú)
# ---------------------------

def ejecutar_explorador(ruta_archivo: str):
    """Controla el menú interactivo y llama a las funciones según la opción elegida"""
    contenido = leer_archivo(ruta_archivo)
    if not contenido:
        return # Si no se puede leer el archivo, se sale
    secciones = extraer_secciones(contenido)

    # Bucle principal del menú
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccioná una opción: ").strip()

        if opcion == '0':
            print("\n¡Hasta luego! 👋")
            break
        elif opcion == '1':
            mostrar_indice(secciones)
        elif opcion == '2':
            termino = input("Término a buscar: ").strip()
            resultados = buscar_en_contenido(secciones, termino)
            for num, sec in resultados:
                print(f"{num}. {sec['titulo']}")
        elif opcion == '3':
            mostrar_indice(secciones)
            try:
                num = int(input("Número de sección: "))
                mostrar_seccion(secciones[num - 1])
            except (ValueError, IndexError):
                print("Número inválido.")
        elif opcion == '4':
            print(contenido)
        elif opcion == '5':
            mostrar_estadisticas(contenido, secciones)
        input("\nPresioná ENTER para continuar...")

# ---------------------------
# Main (punto de inicio del script)
# ---------------------------

if __name__ == "__main__":
    # Configura los argumentos del programa (carpeta y archivo)
    parser = argparse.ArgumentParser(description="Explorador de archivos y documentación - Proyecto Aurelion")
    
    # Parámetro --carpeta o -c → carpeta donde buscar archivos .md
    parser.add_argument("--carpeta", "-c", help="carpeta con archivos .md", default=r"C:\Users\Luna\Desktop\Guayerd\AurelionProyecto")
    
    # Parámetro --file o -f → nombre del archivo específico a abrir
    parser.add_argument("--file", "-f", help="Archivo Markdown a abrir (por defecto se elige del menú)", default=None)
    args = parser.parse_args()

    # Lista los archivos Markdown disponibles en la carpeta indicada
    archivos = listar_archivos(args.carpeta, extension=".md")
    if not archivos:
        print("⚠️ No se encontraron archivos .md en la carpeta indicada.")
        exit()

    # Permite seleccionar cuál archivo abrir
    archivo = args.file or input("Seleccioná el número del archivo a explorar: ").strip()
    if archivo.isdigit():
        archivo = archivos[int(archivo) - 1]

    # Crea la ruta completa y ejecuta el explorador
    ruta = os.path.join(args.carpeta, archivo)
    ejecutar_explorador(ruta)





















