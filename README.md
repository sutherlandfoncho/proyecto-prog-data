# proyecto-prog-data
Programación ciencia de datos

# Análisis de Impacto Operacional y Económico: Rutas Aéreas en Conflictos Geopolíticos

Este proyecto analiza cómo las distintas fases de conflictos geopolíticos (específicamente enfocados en Medio Oriente y periodos de pandemia) afectan la rentabilidad y la logística de las aerolíneas comerciales.

## 🚀 Guía de Instalación y Reproducibilidad

Este proyecto ha sido configurado para ser 100% reproducible mediante entornos virtuales.

### Opción A: Python VENV (Recomendado)
1. Clonar el repositorio.
2. En la terminal, dentro de la carpeta:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt

### Opción B: Conda
    conda env create -f environment.yml
    conda activate scy1101_route

### Estructura del Proyecto
data/:

raw/: Dataset original sin procesar.

processed/: Dataset limpio y validado (route_cost_impact_limpio.csv).

notebooks/:

01_Limpieza_y_Auditoria.ipynb: Preprocesamiento y normalización.

02_transformaciones.ipynb: Ingeniería de variables y análisis de impacto.

03_validacion_entorno_y_reproducibilidad.ipynb: Control de calidad y auditoría.

src/: Código modular en Python (validation.py).

outputs/: Tablas (.csv) y figuras (.png) resultantes del análisis.

### Equipo y Roles
Diego: Especialista en Limpieza y Estándares de Datos.

Alfonso: Analista de Datos y Visualización Estadística.

Cristóbal: QA Engineer, Gestión de Entornos y Reproducibilidad.

---

## 1. Resumen Ejecutivo de Validación
Se ha completado el proceso de validación del proyecto "Análisis de Rutas Aéreas". El flujo de datos es consistente desde la limpieza inicial hasta la generación de gráficos finales.

## 2. Resultados de la Auditoría Técnica
Tras ejecutar el notebook `03_validacion_entorno_y_reproducibilidad.ipynb`, se reportan los siguientes hitos:

* **Integridad de Datos (Checksum):** El archivo `route_cost_impact_limpio.csv` posee el hash `917b25f8fb1858249d875daeea3eeca3`, confirmando que no hubo alteraciones externas.
* **Validación de Reglas de Negocio:** * **Distancia Consistente:** PASÓ (Actual - Original = Extra).
    * **Ingresos Consistentes:** PASÓ (Ticket * Pasajeros = Revenue).
    * **Lógica de Desvíos:** PASÓ (Reroute implica Extra Distance > 0).
* **Consolidación de Filas:** Se mantiene el universo de **3,132 registros**, asegurando que no hubo pérdida de información crítica tras las transformaciones.

## 3. Justificación del Entorno Virtual
Se optó por una estrategia dual (Requirements + Conda) para maximizar la compatibilidad entre distintos sistemas operativos (Windows/Mac/Linux). El uso de un entorno aislado previene conflictos de librerías y garantiza que los gráficos generados por Alfonso se visualicen exactamente igual en cualquier terminal.

## 4. Trazabilidad de Procedencia
Se confirma que los datos originales pasaron por un proceso de limpieza en el Notebook 01, donde se trataron nulos y duplicados. Posteriormente, en el Notebook 02, se calcularon deltas respecto al baseline de la industria, resultados que han sido verificados satisfactoriamente en la fase 03.
