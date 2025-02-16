from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def ensure_unique_department_id(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Ensure that the department_id column is unique by dropping duplicates.
    This simulates the behavior of setting the department_id as a primary key.
    """
    # Drop duplicate rows based on department_id
    df = df.drop_duplicates(subset=['department_id'], keep='first')
    
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert output['department_id'].is_unique, 'department_id is not unique!'
