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
    """
    Execute Transformer Action: ActionType.DROP_DUPLICATE
    and rename columns safely.
    """

    # Drop duplicates
    action = build_transformer_action(
        df,
        action_type=ActionType.DROP_DUPLICATE,
        arguments=df.columns.tolist(),  # Ensure we use a list
        axis=Axis.ROW,
        options={'keep': 'first'},  # Keep the first occurrence of duplicates
    )

    df = BaseAction(action).execute(df)

    # Define the mapping, but only rename existing columns
    column_mapping = {
        'col0': 'order_id',
        'col1': 'user_id',
        'col2': 'order_number',
        'col3': 'order_dow',
        'col4': 'order_hour_of_day',
        'col5': 'days_since_prior_order'
    }

    # Only rename columns that exist in df
    df.rename(columns={k: v for k, v in column_mapping.items() if k in df.columns}, inplace=True)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
