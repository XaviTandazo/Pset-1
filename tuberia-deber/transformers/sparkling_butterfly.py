from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def set_primary_key(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Set the column aisles_id as the primary key by ensuring it contains unique values.
    """
    
    # Ensure aisles_id column has unique values (simulating a primary key constraint)
    if df['aisles_id'].duplicated().any():
        raise ValueError("The aisles_id column contains duplicates. It must be unique to be a primary key.")
    
    # Set aisles_id as the index, but retain the column in the DataFrame
    df.set_index('aisles_id', inplace=True, drop=False)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
