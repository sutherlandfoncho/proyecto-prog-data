# Diccionario de Datos
**Dataset:** `route_cost_impact_limpio.csv`
**Responsable de auditoría:** Diego

| Variable | Tipo Final | Descripción | Transformación Aplicada | Observaciones Importantes |
| :--- | :--- | :--- | :--- | :--- |
| `month` | datetime64 | Fecha (Año y Mes) del registro | Convertido de string a datetime. | Clave para analizar series de tiempo y evolución de crisis. |
| `conflict_phase` | object (str) | Etapa de crisis (ej. Pandemia, Guerra) | Ninguna. | Variable fundamental para agrupar los impactos. |
| `airline` / `iata_code` | object (str) | Nombre y código de la aerolínea | Ninguna. | Sin valores nulos detectados. |
| `origin_city` / `destination_city` | object (str) | Ciudades de la ruta de vuelo | Ninguna. | - |
| `aircraft_type` | object (str) | Modelo del avión utilizado | Ninguna. | - |
| `original_distance_km` | int64 | Distancia normal de la ruta | Ninguna. | - |
| `actual_distance_km` | float64 | Distancia real volada | Ninguna. | Contiene outliers válidos por desvíos. |
| `extra_distance_km` | float64 | Kilómetros extra por desvíos | Ninguna. | Contiene 116 outliers válidos (impacto de conflictos). |
| `rerouted` / `flight_cancelled` | object (str) | Indicadores de desvío o cancelación | Ninguna. | - |
| `fuel_consumption_bbl` | float64 | Consumo de combustible en barriles | Ninguna. | - |
| `brent_crude_usd` | float64 | Precio del barril de petróleo | Ninguna. | Presenta picos históricos (outliers no eliminados). |
| `jet_fuel_usd_barrel` | float64 | Precio del combustible de avión | Imputación preventiva por la media. | Contiene 180 outliers conservados intencionalmente. |
| `total_fuel_cost_usd` | float64 | Costo total de combustible | Ninguna. | - |
| `extra_fuel_cost_usd` | float64 | Costo extra por desvíos | Ninguna. | - |
| `base_ticket_price_usd` | float64 | Precio base del pasaje | Ninguna. | - |
| `fuel_surcharge_usd` | float64 | Recargo cobrado por combustible | Ninguna. | - |
| `total_ticket_price_usd` | float64 | Precio final del pasaje | Imputación preventiva por la media. | Conserva variabilidad real de las crisis. |
| `estimated_passengers` | int64 | Cantidad de pasajeros | Ninguna. | Muestra caídas drásticas (ej. durante pandemia). |
| `route_revenue_usd` | float64 | Ingresos totales de la ruta | Ninguna. | - |
| `fuel_pct_of_cost` | float64 | Porcentaje del costo que es combustible| Ninguna. | - |

**Nota de Integridad:** Se aplicó `drop_duplicates()` de forma preventiva en el pipeline, asegurando 0 filas duplicadas en la versión final.