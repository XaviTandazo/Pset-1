from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def rename_columns(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: Rename columns (col0 and col1)

    Renames col0 to aisle_id and col1 to aisle
    """
    # Construir la acción de renombrar las columnas
    action = build_transformer_action(
        df,
        action_type=ActionType.RENAME_COLUMNS,
        arguments=['col0', 'col1'],  # Especificar las columnas que se van a renombrar
        axis=Axis.COLUMN,
        options={'rename': {'col0': 'aisle_id', 'col1': 'aisle'}},  # Nuevos nombres para las columnas
    )

    return BaseAction(action).execute(df)
