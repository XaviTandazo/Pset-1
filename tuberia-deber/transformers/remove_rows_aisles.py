from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:

    df = df.dropna(subset=['aisles'])  #Eliminar valores nulos en 'aisle'
    df = df[df['aisles'] != 'missing']  #Eliminar filas donde 'aisle' sea 'missing'

    action = build_transformer_action(
        df,
        action_type=ActionType.FILTER,  
        axis=Axis.ROW,
        options={
            'conditions': [{'column': 'aisles', 'condition': 'not_null'}],
        },
    )

    return BaseAction(action).execute(df)


@test
def test_output(output, *args) -> None:

    assert output['aisles'].isnull().sum() == 0, 'Todav�a hay valores nulos en la columna aisle'
    assert (output['aisles'] == 'missing').sum() == 0, "Todav�a hay filas con 'missing' en la columna aisle"
