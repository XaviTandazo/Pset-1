if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(df: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
    # Handle missing values
    df = df.fillna(0)  # Replace NaN with 0, or use appropriate method

    # Remove duplicates
    df = df.drop_duplicates()

    # Generate derived columns (example: date/time format)
    if 'date_column' in df.columns:
        df['formatted_date'] = pd.to_datetime(df['date_column'])

    # Map to correct data types
    df['aisle_id'] = df['aisle_id'].astype(int)
    df['aisle'] = df['aisle'].astype(str)

    # Model the table (dimension in this case)
    df = df.rename(columns={'aisle_id': 'aisle_key'})

    # Additional transformations can be added here

    return df

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
    assert isinstance(output, pd.DataFrame), 'The output is not a DataFrame'
    assert 'aisle_key' in output.columns, 'The output does not have the expected columns'