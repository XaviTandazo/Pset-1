from mage_ai.data_preparation.decorators import transformer
import pandas as pd

# Decorar correctamente la funci�n con @transformer
@transformer
def transform_data(df: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
    """
    Esta funci�n transforma los datos para cumplir con los siguientes objetivos:
    - Asegurar que 'col0' tenga tipo de dato num�rico.
    - Asegurar que 'col1' sea de tipo texto.
    - Eliminar filas con valores faltantes en 'col0'.
    """
    # Asegurarse de que 'col0' tenga tipo de dato entero (por ejemplo, si son IDs o n�meros)
    df['col0'] = pd.to_numeric(df['col0'], errors='coerce')  # Convierte a num�rico, y si hay errores, los reemplaza por NaN

    # Asegurarse de que 'col1' tenga tipo de dato de texto (si es una descripci�n o categor�a)
    df['col1'] = df['col1'].astype(str)  # Convierte todo a cadena de texto

    # Opcional: Eliminar filas con valores NaN en 'col0' (si los hubiere despu�s de la conversi�n)
    df = df.dropna(subset=['col0'])

    return df
