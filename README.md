
# proyecto-prog-data
Programación ciencia de datos

# Análisis de Impacto Operacional y Económico: Rutas Aéreas en Conflictos Geopolíticos

Este proyecto analiza cómo las distintas fases de conflictos geopolíticos (enfocados en Medio Oriente) y periodos de crisis sanitaria afectan la rentabilidad y logística de las aerolíneas comerciales. Se enfoca en cuantificar desvíos de rutas, variaciones en costos de combustible e ingresos por trayecto.
## 🚀 Guía de Instalación y Reproducibilidad

El proyecto utiliza entornos aislados para garantizar que las dependencias no generen conflictos con el sistema local y que los resultados sean consistentes en cualquier máquina.

### Opción A: Python VENV (Recomendado para entornos ligeros)
Ideal si ya tienes Python instalado. Este método descarga las librerías necesarias en una carpeta local .venv.
1. Clonar el repositorio.
2. En la terminal, dentro de la carpeta:
   ```bash
   # creamos el entorno
   python -m venv .venv  
   # activamos el entorno
    # En Windows:
    .venv\Scripts\activate 
    # En Mac/Linux:
    source .venv/bin/activate

   # instalamos las dependencias 
   pip install -r requirements.txt 

### Opción B: Conda (Recomendado para análisis de datos avanzado)
Ideal para gestionar versiones de Python y librerías científicas de forma robusta.
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

### Flujo de trabajo
El proyecto se divide en tres bloques técnicos para asegurar la trazabilidad del dato:

Data Engineering (Diego): Responsable de la ingesta y auditoría inicial. Se asegura de que el dato sea confiable y estandarizado.

Data Analysis (Alfonso): Encargado de convertir el dato limpio en insights. Crea KPIs como extra_fuel_cost y visualiza tendencias económicas.

QA & DevOps (Cristóbal): Garantiza que el proyecto sea reproducible. Implementa validaciones automáticas y gestiona la configuración de los entornos virtuales.

---

## 1. Resumen Ejecutivo de Validación
Se ha completado el proceso de validación del proyecto "Análisis de Rutas Aéreas". El flujo de datos es consistente desde la limpieza inicial hasta la generación de gráficos finales.

## 2. Resultados de la Auditoría Técnica
Tras ejecutar el notebook `03_validacion.ipynb`, se reportan los siguientes hitos:

 **Integridad de Datos (Checksum):** El archivo `route_cost_impact_limpio.csv` posee el hash `917b25f8fb1858249d875daeea3eeca3`, confirmando que no hubo alteraciones externas.
 **Validación de Reglas de Negocio:** * **Distancia Consistente:** PASÓ (Actual - Original = Extra).
     **Ingresos Consistentes:** PASÓ (Ticket * Pasajeros = Revenue).
     **Lógica de Desvíos:** PASÓ (Reroute implica Extra Distance > 0).
 **Consolidación de Filas:** Se mantiene el universo de **3,132 registros**, asegurando que no hubo pérdida de información crítica tras las transformaciones.

## 3. Justificación del Entorno Virtual
Se optó por una estrategia dual (Requirements + Conda) para maximizar la compatibilidad entre distintos sistemas operativos (Windows/Mac/Linux). El uso de un entorno aislado previene conflictos de librerías y garantiza que los gráficos generados por Alfonso se visualicen exactamente igual en cualquier terminal.

## 4. Trazabilidad de Procedencia
Se confirma que los datos originales pasaron por un proceso de limpieza en el Notebook 01, donde se trataron nulos y duplicados. Posteriormente, en el Notebook 02, se calcularon deltas respecto al baseline de la industria, resultados que han sido verificados satisfactoriamente en la fase 03.
