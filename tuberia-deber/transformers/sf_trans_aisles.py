from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from os import path
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def connect_to_aisles_table(*args, **kwargs) -> DataFrame:
    """
    Connect to Snowflake and fetch data from the aisles table.
    Add primary keys based on the provided column (col0).
    """
    query = 'SELECT * FROM INSTACART_DB.RAW.AISLES'
    config_path = path.join('C:\\Users\\Paul Tandazo\\Documents\\deber1-data\\personal-data-engine\\personal-data-engine', 'io_config.yaml')
    config_profile = 'default'

    with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        aisles_df = loader.load(query)
        
        # Asignar una columna primary_key basada en el índice (col0)
        aisles_df['primary_key'] = aisles_df['col0']
        
        return aisles_df


@test
def test_output(output, *args) -> None:
    """
    Test to ensure the data is fetched correctly from the aisles table
    and that the primary key is assigned correctly.
    """
    assert isinstance(output, DataFrame), 'Output is not a DataFrame'
    assert not output.empty, 'The result is empty, no data fetched from the aisles table'
    assert 'primary_key' in output.columns, 'Primary key is not assigned'
    assert output['primary_key'].equals(output['col0']), 'Primary key does not match col0'
