from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from os import path
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform_in_snowflake(*args, **kwargs) -> DataFrame:
    """
    Cleans and transfers data from 'raw' schema to 'clean' schema in Snowflake.
    - Removes duplicates based on order_id.
    - Filters out outliers in order_number and order_hour_of_day.
    - Ensures primary key on order_id in destination table.
    """
    config_path = path.join('C:\\Users\\Paul Tandazo\\Documents\\deber1-data\\personal-data-engine\\personal-data-engine', 'io_config.yaml')
    config_profile = 'default'

    query = '''
    -- Step 1: Ensure the clean table exists with a primary key
    CREATE TABLE IF NOT EXISTS clean.instacart_orders (
        order_id INT PRIMARY KEY,
        user_id INT NOT NULL,
        order_number INT NOT NULL CHECK (order_number BETWEEN 1 AND 50),
        order_dow INT NOT NULL CHECK (order_dow BETWEEN 0 AND 6),
        order_hour_of_day INT NOT NULL CHECK (order_hour_of_day BETWEEN 0 AND 23),
        days_since_prior_order FLOAT
    );

    -- Step 2: Insert cleaned data from raw schema
    INSERT INTO clean.instacart_orders (order_id, user_id, order_number, order_dow, order_hour_of_day, days_since_prior_order)
    SELECT DISTINCT
        order_id,
        user_id,
        order_number,
        order_dow,
        order_hour_of_day,
        days_since_prior_order
    FROM raw.instacart_orders
    WHERE order_number BETWEEN 1 AND 50 -- Remove outliers in order_number
    AND order_hour_of_day BETWEEN 0 AND 23; -- Remove outliers in order_hour_of_day
    '''

    sample_table = 'instacart_orders'
    sample_schema = 'clean'
    sample_size = 10_000

    with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.execute(query)
        loader.commit()  # Apply changes permanently
        return loader.sample(sample_schema, sample_size, sample_table)

@test
def test_output(output, *args) -> None:
    """
    Test to check if the transformation output is valid.
    """
    assert output is not None, 'The output is undefined'
    assert len(output) > 0, 'No data was moved to the clean schema'
