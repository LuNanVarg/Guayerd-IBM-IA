
📝 Directrices – Proyecto Aurelion

---

## 🟢 Preparación del Entorno

Antes de comenzar, asegurate de tener todo listo:

### 💻 Software Requerido

* Python ≥ 3.8
* Editor recomendado: VS Code o PyCharm

### 📦 Instalación de Dependencias

```bash
pip install pandas numpy openpyxl matplotlib seaborn
```

---

## 📁 Estructura de Carpetas

```
AurelionProyecto/
│
├── README.md                      # Manual y descripción del proyecto
├── Informe.md                     # Documento principal del proyecto
├── Directrices.md                 # Este archivo
├── Interactivo_LeerArchivo.py     # Programa interactivo de Menú (Lectura/Carga/Merge)
├── ExploradorDoc.py               # Programa interactivo de documentación
├── Limpiar_Datos.py               # Módulo Lógica: Contiene la función Limpiar_Datos (ETL)
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

## 🟡 Verificación de Archivos

| Archivo                          | Función                                      |
| -------------------------------- | -------------------------------------------- |
| `ExploradorDoc.py`               | Programa interactivo de documentación        |
| `Interactivo_LeerArchivo.py`     | Script principal con el menú interactivo     |
| `Limpiar_Datos.py`               | Módulo de Lógica (ETL, Merge y Validaciones) |
| `AnalisisVenta.ipynb`            | Notebook con visualizaciones y KPIs          |
| `Aurelion/`                      | Carpeta con archivos de datos (`csv`)        |
| `FlujoDelProceso.drawio`         | Diagrama de flujo del programa               |
| `Informe.md`                     | Documento principal del proyecto             |

---

## 🔵 Ejecución del Programa Interactivo

1. Abrir terminal en la carpeta raíz `AurelionProyecto/`.
2. Ejecutar:

```bash
python ExploradorDoc.py
```

3. Navegar usando el menú interactivo:

* Introducción
* Creación de carpetas y descarga de archivos
* Descripción de tablas
* Requisitos técnicos y validaciones
* Definición del problema y solución
* Diagrama de flujo
* Pseudocódigo

4. Para salir, seleccionar **Exit**

> ⚠️ Tip: Usar flechas o números para navegar más rápido

---

## 🟠 Validaciones de Calidad de Datos

Antes de generar análisis o reportes, verificar:

* 📅 Fechas y números en formato correcto
* 🔍 Eliminación de duplicados en campos clave
* 💰 Precios e importes positivos y consistentes
* ⏳ Fecha de alta del cliente anterior a compras; sin fechas futuras
* 🔗 Integridad referencial entre tablas

> ✅ Estas validaciones aseguran la confiabilidad de los KPIs

---

## 🟣 Uso de la Documentación

* Seguir el flujo sugerido para comprender el proyecto
* Revisar secciones críticas antes de generar análisis
* Confirmar que los datos nuevos cumplen con formatos y validaciones

---

## 🟤 Checklist de Entrega del Sprint

* ✅ Verificar estructura de carpetas y archivos
* ✅ Pseudocódigo y diagrama reflejan validaciones de datos
* ✅ Programa interactivo funciona correctamente

---

## 🔴 Soporte y Contacto

* ✉️ Correo: `nancy.vargas.it@gmail.com`
* 💬 Discord: `nancyvargas22039`

---

## ⚡ Notas Finales

* Este manual se actualizará con nuevas versiones del proyecto
* Marcar cada sección completada para garantizar correcta implementación
* **Recomendación:** leer antes de ejecutar para evitar errores

---

### 💬 Créditos

📌 **Autora:** Nancy Vargas
🎓 **Curso:** Fundamentos de Inteligencia Artificial – Guayerd & IBM SkillsBuild
📅 **Año:** 2025
💻 **Lenguaje:** Python 3.x
📚 **Temática:** Integración y análisis de datos de ventas

---

