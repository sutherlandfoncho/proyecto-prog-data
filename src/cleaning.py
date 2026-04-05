import pandas as pd
import numpy as np

def cargar_datos(ruta):
    """Carga el dataset desde un archivo CSV."""
    print(f"Cargando datos desde: {ruta}")
    return pd.read_csv(ruta)

def auditar_datos(df):
    """Realiza una revisión inicial del dataset."""
    print("\n--- AUDITORÍA INICIAL ---")
    print(f"Dimensiones: {df.shape}")
    print(f"Nulos totales: {df.isnull().sum().sum()}")
    print(f"Duplicados totales: {df.duplicated().sum()}")

def limpiar_y_formatear(df):
    """Aplica la eliminación de duplicados, imputación y formatos."""
    df_clean = df.copy()
    
    # 1. Duplicados
    df_clean = df_clean.drop_duplicates()
    
    # 2. Imputación preventiva (media)
    columnas_imputar = ['jet_fuel_usd_barrel', 'total_ticket_price_usd']
    for col in columnas_imputar:
        df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
        
    # 3. Formato de fechas
    df_clean['month'] = pd.to_datetime(df_clean['month'])
    
    return df_clean

def detectar_outliers(df, columnas):
    """Detecta outliers usando el método IQR y reporta los totales."""
    print("\n--- DETECCIÓN DE OUTLIERS (IQR) ---")
    total_outliers = 0
    for col in columnas:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        
        outliers = df[(df[col] < limite_inferior) | (df[col] > limite_superior)]
        if len(outliers) > 0:
            print(f"🔹 {col}: {len(outliers)} valores atípicos.")
            total_outliers += len(outliers)
            
    print(f"Total general detectado: {total_outliers}")
    print("Nota: Conservados intencionalmente por ser extremos plausibles de crisis.")

def guardar_datos(df, ruta_salida):
    """Exporta el dataframe limpio a un nuevo CSV."""
    df.to_csv(ruta_salida, index=False)
    print(f"\nArchivo limpio guardado exitosamente en: {ruta_salida}")

# Ejecución principal (Pipeline)
if __name__ == "__main__":
    # 1. Cargar
    df_raw = cargar_datos("../data/raw/route_cost_impact.csv")
    
    # 2. Auditar
    auditar_datos(df_raw)
    
    # 3. Limpiar
    df_procesado = limpiar_y_formatear(df_raw)
    
    # 4. Outliers
    columnas_num = ['actual_distance_km', 'extra_distance_km', 'fuel_consumption_bbl',
                    'brent_crude_usd', 'jet_fuel_usd_barrel', 'total_fuel_cost_usd',
                    'extra_fuel_cost_usd', 'total_ticket_price_usd', 'fuel_surcharge_usd',
                    'estimated_passengers', 'route_revenue_usd', 'fuel_pct_of_cost']
    detectar_outliers(df_procesado, columnas_num)
    
    # 5. Guardar
    guardar_datos(df_procesado, "../data/processed/route_cost_impact_limpio.csv")