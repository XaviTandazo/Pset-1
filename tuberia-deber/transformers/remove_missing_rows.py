from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Elimina las filas que contengan valores missing en cualquiera de las columnas.
    """
    df = df.dropna()  # Elimina las filas con valores faltantes en cualquier columna

    return df


@test
def test_output(output, *args) -> None:
    """
    Verifica que no haya filas con valores missing en el DataFrame de salida.
    """
    assert not output.isnull().values.any(), "Todavía hay filas con valores missing"
