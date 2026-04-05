Informe Técnico: Impacto de Conflictos Geopolíticos en el Transporte Aéreo
Curso: SCY1101

Equipo: Diego (Data Engineer), Alfonso (Data Analyst), Cristóbal (QA & DevOps)

1. Introducción
Este proyecto surge de la necesidad de cuantificar el impacto operacional y económico que los eventos geopolíticos de gran escala y las crisis sanitarias (COVID-19) ejercen sobre las rutas comerciales. Se analizó un dataset de 3,132 vuelos, evaluando variables de costo, distancia y consumo de combustible en diferentes fases críticas.

2. Metodología y Flujo de Trabajo
El proyecto se dividió en tres etapas interconectadas para garantizar la calidad del producto final:

2.1. Procesamiento y Limpieza (Fase 01 - Diego)
Se realizó una auditoría inicial del dataset raw para corregir inconsistencias.

Normalización: Formateo de fechas y estandarización de nombres de aerolíneas.

Tratamiento de Datos: Eliminación de registros duplicados y gestión de valores nulos en columnas críticas como total_fuel_cost_usd.

Resultado: Un dataset limpio y listo para el análisis con 3,132 registros íntegros.

2.2. Análisis y Transformación (Fase 02 - Alfonso)
En esta etapa se generó la inteligencia de negocio a partir de los datos limpios.

Ingeniería de Variables: Creación de indicadores como is_disrupted, extra_fuel_cost e ingresos por pasajero.

Análisis de Impacto: Cálculo de deltas respecto al baseline pre-pandemia. Se identificó que la fase US-Iran War fue el punto de mayor estrés operacional, con el máximo de extra_distance_km.

Visualización: Generación de matrices de correlación y gráficos de tendencia que muestran la recuperación de ingresos post-COVID frente al aumento de costos operativos.

2.3. Validación y Reproducibilidad (Fase 03 - Cristóbal)
Como cierre del proyecto, se implementó un sistema de garantía de calidad.

Entorno Técnico: Configuración de requirements.txt y environment.yml para permitir la ejecución del proyecto en cualquier máquina sin errores de dependencias.

Auditoría de Integridad: Uso de Checksums MD5 para asegurar que los datos no sufrieron alteraciones entre fases.

Validación de Reglas de Negocio: Verificación automatizada de que los cálculos financieros (Revenue) y operacionales (Distancias) guardan una relación lógica estricta.

3. Resultados Principales
Correlación de Costos: Se comprobó una relación directa entre el aumento del crudo Brent y los recargos por combustible aplicados a los tickets.

Resiliencia Operacional: A pesar de los desvíos (rerouting) en zonas de conflicto, la industria mantuvo una eficiencia de ingresos positiva en rutas de larga distancia.

Validación Exitosa: El 100% de las pruebas de integridad y lógica de negocio pasaron satisfactoriamente, certificando la fidelidad de los gráficos y conclusiones presentadas.

4. Conclusiones
La estructura modular del proyecto permitió transformar datos raw en información estratégica validada. La combinación de una limpieza rigurosa, un análisis estadístico profundo y una validación técnica final asegura que este informe sea una base sólida para la toma de decisiones en logística aérea.