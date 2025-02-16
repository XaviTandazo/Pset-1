from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    
    if 'department' in df.columns:
        df['department'] = df['department'].str.title()  #Capitaliza cada palabra

    return df


@test
def test_output(output, *args) -> None:
    assert output['department'].str.istitle().all(), "Algunos valores en 'aisle' no están capitalizados correctamente"
