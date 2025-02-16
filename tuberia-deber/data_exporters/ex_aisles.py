from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_snowflake(df: DataFrame, **kwargs) -> None:
    """
    Export data from Mage AI pipeline to Snowflake warehouse.
    Ensure your configuration settings in 'io_config.yaml' are correct.
    """
    table_name = 'AISLES'  # Nombre de la tabla de destino en Snowflake
    database = 'INSTACART_DB'  # Base de datos de destino
    schema = 'RAW'  # Esquema de destino
    config_path = path.join('C:\\Users\\Paul Tandazo\\Documents\\deber1-data\\personal-data-engine\\personal-data-engine', 'io_config.yaml')
    config_profile = 'default'  # Perfil de configuración en io_config.yaml

    # Conectar a Snowflake con la configuración proporcionada
    with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        # Exportar el DataFrame 'df' a la tabla en Snowflake
        loader.export(
            df,
            table_name,
            database,
            schema,
            if_exists='replace',  # Especifica la política si la tabla ya existe
        )
