from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_snowflake(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Snowflake warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#snowflake
    """
    # Especifica el nombre de la tabla, la base de datos y el esquema en Snowflake
    table_name = 'instacart_orders'  # Nombre de la tabla de destino
    database = 'instacart_db'        # Nombre de la base de datos
    schema = 'public'                # Esquema dentro de la base de datos

    # Carga la configuración desde el archivo io_config.yaml
    config_path = path.join('C:\\Users\\Paul Tandazo\\Documents\\deber1-data\\personal-data-engine\\personal-data-engine', 'io_config.yaml')
    onfig_profile = 'default'

    # Exporta los datos a Snowflake
    with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,                     # DataFrame que deseas exportar
            table_name,             # Nombre de la tabla de destino
            database,               # Base de datos de destino
            schema,                 # Esquema de destino
            if_exists='replace',    # Qué hacer si la tabla ya existe (opciones: 'replace', 'append', etc.)
        )
