from mage_ai.data_preparation.decorators import transformer
import pandas as pd

@transformer
def transform_data(df: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
    """
    Transforma los datos extraídos del esquema RAW aplicando limpieza y modelado.
    """

    # 1. Manejar valores faltantes
    df.fillna({'nombre_columna': 'Valor por defecto'}, inplace=True)  # Rellenar valores nulos
    df.dropna(subset=['columna_importante'], inplace=True)  # Eliminar filas con valores nulos en una columna clave

    # 2. Eliminar duplicados
    df.drop_duplicates(inplace=True)

    # 3. Generar columnas derivadas (ejemplo: formato fecha/hora)
    df['fecha_formateada'] = pd.to_datetime(df['fecha_original'], format='%Y-%m-%d')

    # 4. Mapear a los tipos de datos correctos
    df['cantidad'] = df['cantidad'].astype(int)
    df['precio'] = df['precio'].astype(float)

    # 5. Modelado: Identificar si es una tabla de dimensión o de hechos
    if 'venta_id' in df.columns:  # Si la tabla tiene IDs de transacciones, es una tabla de hechos
        table_name = 'fact_ventas'
    else:
        table_name = 'dim_productos'

    # 6. Agregar metadatos o asignar nombre a la tabla
    df.attrs['table_name'] = table_name

    return df

