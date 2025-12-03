

# 🌌 Proyecto Aurelion

### Descripción general

El **Proyecto Aurelion** forma parte del curso *Fundamentos de Inteligencia Artificial* impulsado por **Guayerd & IBM SkillsBuild (2025)**.
Su objetivo es integrar, limpiar y analizar datos de ventas mediante un programa en **Python** que permite navegar la documentación técnica del proyecto desde la terminal de forma interactiva.

---

### 🧩 Estructura del Proyecto


```
AurelionProyecto/
│
├── README.md                      # Este archivo
├── Informe.md                     # Documento principal del proyecto
├── Directrices.md                 # Registro del análisis y mejoras
├── InteractivoLeer.py             # Módulo para lectura y carga de archivos
├── ExploradorDoc.py               # Navegador interactivo de documentación
├── LeerArchivo.py                 # Módulo para lectura y carga de archivos
├── AnalisisVenta.ipynb            # Notebook interactivo con gráficos y KPIs
│
├── FlujoDelProceso.drawio         # Diagrama del flujo del programa
│
└── Aurelion/                      # Carpeta de datos
   ├── clientes.csv                # Base de datos de clientes
   ├── productos.csv               # Base de datos de productos
   ├── ventas.csv                  # Base de datos de ventas
   └── detalle_ventas.csv          # Base de datos de detalle de ventas

```

---

### ⚙️ Requisitos previos

Asegurate de tener instalado **Python 3.8 o superior** y las siguientes bibliotecas:

```bash
pip install pandas numpy openpyxl matplotlib seaborn
```

---

### 🚀 Cómo ejecutar el programa

🖥️ Modo terminal
1. Abrí una terminal (CMD, PowerShell o desde Visual Studio Code).
2. Navegá hasta la carpeta del proyecto:

   ```bash
   cd "ruta\a\AurelionProyecto"
   ```

3. Ejecutá el programa interactivo:

   ```bash
python ExploradorDoc.py
   ```

---

### 🧭 Uso del programa interactivo

El sistema lee el archivo `Documentación-v2.md` y genera un **menú interactivo** que te permite recorrer sus secciones.
Podés explorar la información con las siguientes opciones:

* Ingresar un número para abrir una sección o subsección.
* Presionar `Enter` para avanzar página, `b` para retroceder y `q` para volver al menú anterior.
* Ingresar `0` para salir del programa.

💡 *El contenido se actualiza automáticamente cada vez que se modifica el archivo `Documentación-v2.md`.*

---

📊 Modo interactivo (Jupyter Notebook)

Abrí Jupyter y cargá AnalisisVenta.ipynb.

Ejecutá las celdas en orden para explorar datos, generar gráficos y navegar la documentación con widgets interactivos.

---

### 🔍 Funcionalidades principales

* **Explorar documentación técnica desde la terminal.**
* **Interfaz interactiva en Jupyter con filtros y gráficos.**
* **Análisis de ventas por cliente, producto, ciudad y medio de pago.**
* **KPIs automáticos: ticket promedio, total vendido, clientes inactivos.**
* **Limpieza, validación y resumen de datos.**
* **Compatibilidad multiplataforma (Windows / Linux / macOS).**

---

### 📊 Alcance del Proyecto

El programa integra y analiza información de cuatro bases de datos:

* `clientes.xlsx`
* `productos.xlsx`
* `ventas.xlsx`
* `detalle_ventas.xlsx`

Permite generar reportes y métricas clave como:

* Ventas por cliente, categoría, medio de pago y ciudad.
* Ingreso total, ticket promedio y clientes inactivos.
* Validaciones de calidad de datos y consistencia referencial.

---

### 🧱 Modelos incluidos

* **Modelo Conceptual (ER):** Relaciones entre Clientes, Ventas, Detalle_Ventas y Productos.
* **Modelo Lógico:** Definición de tablas y claves principales/foráneas.
* **Modelo Físico:** Representación de las bases de datos en formato `.csv`.
* **Diagrama de Flujo del Programa:** Descripción paso a paso del proceso de integración y análisis.

---

### 💬 Créditos

📌 **Autora:** Nancy Vargas
🎓 **Curso:** Fundamentos de Inteligencia Artificial – Guayerd & IBM SkillsBuild
📅 **Año:** 2025
💻 **Lenguaje:** Python 3.x
📚 **Temática:** Integración y análisis de datos de ventas
🎨 **Formatos:** CLI + Jupyter Notebook

---
