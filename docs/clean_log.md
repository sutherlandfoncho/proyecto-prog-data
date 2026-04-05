"Limpieza de datos"

Diego Echeverría
Dataset: route_cost_impact.csv

1. Auditoría Inicial
- Problema detectado: Se realizó una revisión al dataset en busca de valores nulos, filas duplicadas, en este caso el dataset estaba en excelentes condiciones, arrojando 0 valores nulos y 0 filas duplicadas.
- Decisión tomada: Se incluyerón de todas formas las funciones 'drop_duplicates()' e imputación por la media ('fillna') en el pipeline de la limpieza. 
- Justificación: Aunque no habían nulos y duplicados actualesm establecer estas reglas asegura que en el futuro aunque se inyecten datos sucios, el pipeline no fallará y los tratará automáticamente.
- Impacto esperado: Garantiza la robustez y automatización del flujo de trabajo continuo. 

2. Tipificación de Datos (Ruido y Formatos)
- Problema detectado: La variable temporal `month` venía en formato de texto (ej. "2019-01"), lo cual impide el análisis cronológico.
- Decisión tomada: Se transformó la columna completa al formato oficial `datetime` de Pandas.
- Justificación: Los modelos predictivos y las herramientas de visualización requieren formatos temporales estandarizados para graficar tendencias y entender el paso del tiempo.
- Impacto esperado:** Permite a los analistas posteriores agrupar costos e ingresos por trimestre o año sin errores de lectura.

3. Detección de Valores Atípicos (Outliers)
- Problema detectado: Al auditar variables financieras y operativas con el método IQR (Rango Intercuartílico), se detectaron 1328 valores extremos (ej. 216 en `brent_crude_usd` y 116 en `extra_distance_km`).
- Decisión tomada: NO se eliminó ni modificó ningún outlier.
- Justificación: Estos valores no son errores de digitación, sino "extremos plausibles". Representan el impacto real de las variables `conflict_phase` (pandemia, guerras), donde los desvíos de ruta y los picos en el valor del barril de petróleo ocurrieron en la realidad.
- Impacto esperado: Mantener esta variabilidad permite que el modelo de Machine Learning aprenda cómo reaccionan los costos de la aerolínea frente a escenarios de crisis mundiales reales.