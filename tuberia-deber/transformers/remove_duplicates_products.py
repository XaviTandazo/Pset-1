from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Elimina las filas duplicadas de la tabla.
    """
    df = df.drop_duplicates()  # Elimina filas duplicadas en todas las columnas

    return df


@test
def test_output(output, *args) -> None:
    """
    Verifica que no haya duplicados en el DataFrame de salida.
    """
    assert not output.duplicated().any(), "Todav�a hay filas duplicadas en la tabla"
