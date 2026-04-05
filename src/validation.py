import pandas as pd
import numpy as np
import hashlib

def calcular_checksum(file_path):
    """Genera un hash MD5 para verificar la integridad del archivo."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def validar_reglas_negocio(df):
    """Aplica las reglas lógicas definidas en el proyecto."""
    resultados = {}
    
    # 1. Validación de distancia extra
    # actual - original debe ser igual a extra
    diff_dist = (df['actual_distance_km'] - df['original_distance_km']) - df['extra_distance_km']
    resultados['distancia_consistente'] = diff_dist.abs().max() < 0.01
    
    # 2. Validación de Ingresos (Precio * Pasajeros)
    # Permitimos un margen de error de 1 USD por redondeos
    diff_rev = (df['total_ticket_price_usd'] * df['estimated_passengers']) - df['route_revenue_usd']
    resultados['ingresos_consistentes'] = diff_rev.abs().max() < 1.0
    
    # 3. Regla Lógica de Rerouted
    # Si rerouted == 'Yes', extra_distance_km debe ser > 0
    anomalias_reroute = df[(df['rerouted'] == 'Yes') & (df['extra_distance_km'] <= 0)]
    resultados['reroute_logico'] = len(anomalias_reroute) == 0
    
    return resultados

def check_calidad_basica(df):
    """Revisa nulos y duplicados."""
    return {
        "nulos": df.isnull().sum().sum(),
        "duplicados": df.duplicated().sum(),
        "filas": len(df),
        "columnas": len(df.columns)
    }


"""Este código automatiza la auditoría del proyecto.
Primero, el Checksum garantiza que los archivos son auténticos (Integridad).
Segundo, las Reglas de Negocio aseguran que los datos financieros y operacionales son coherentes entre sí (Consistencia).
Y tercero, el Check de Calidad monitorea que no hayamos introducido ruido como duplicados o nulos durante el proceso."""