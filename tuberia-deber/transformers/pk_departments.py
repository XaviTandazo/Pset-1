from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def assert_unique_department_id(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Assert that the department_id column contains unique values (simulating a primary key).
    """
    # Assert that the department_id is unique
    assert df['department_id'].is_unique, 'department_id is not unique!'

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
