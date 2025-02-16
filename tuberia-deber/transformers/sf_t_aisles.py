from mage_ai.data_preparation.decorators import transformer

@transformer
def transform_aisles(df, *args, **kwargs):
    """
    Limpia y transforma los datos de la tabla AISLES.
    """
    print("Ejecutando transformación en la tabla AISLES...")
    print(df.head())  # Verifica que los datos estén cargando

    # Renombrar columnas
    df.rename(columns={
        'aisle_id': 'id_pasillo',
        'aisle': 'nombre_pasillo'
    }, inplace=True)

    # Eliminar filas con valores nulos
    df = df.dropna()

    return df
