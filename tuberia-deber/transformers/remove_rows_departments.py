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

    df = df.dropna(subset=['department'])  
    df = df[df['department'] != 'missing']  #Eliminar filas donde 'aisle' sea 'missing'

    action = build_transformer_action(
        df,
        action_type=ActionType.FILTER,  
        axis=Axis.ROW,
        options={
            'conditions': [{'column': 'department', 'condition': 'not_null'}],
        },
    )

    return BaseAction(action).execute(df)


@test
def test_output(output, *args) -> None:

    assert output['department'].isnull().sum() == 0, 'Todavía hay valores nulos en la columna aisle'
    assert (output['department'] == 'missing').sum() == 0, "Todavía hay filas con 'missing' en la columna aisle"
