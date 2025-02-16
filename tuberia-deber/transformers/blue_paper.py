from mage_ai.data_preparation.decorators import transformer
import pandas as pd

# Decorar correctamente la función con @transformer
@transformer
def transform_data(df: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
    """
    Esta función transforma los datos para cumplir con los siguientes objetivos:
    - Asegurar que 'col0' tenga tipo de dato numérico.
    - Asegurar que 'col1' sea de tipo texto.
    - Eliminar filas con valores faltantes en 'col0'.
    """
    # Asegurarse de que 'col0' tenga tipo de dato entero (por ejemplo, si son IDs o números)
    df['col0'] = pd.to_numeric(df['col0'], errors='coerce')  # Convierte a numérico, y si hay errores, los reemplaza por NaN

    # Asegurarse de que 'col1' tenga tipo de dato de texto (si es una descripción o categoría)
    df['col1'] = df['col1'].astype(str)  # Convierte todo a cadena de texto

    # Opcional: Eliminar filas con valores NaN en 'col0' (si los hubiere después de la conversión)
    df = df.dropna(subset=['col0'])

    return df
