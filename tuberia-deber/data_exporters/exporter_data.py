from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from os import path

def test_snowflake_connection():
    config_path = path.join('C:\\Users\\Paul Tandazo\\Documents\\deber1-data\\personal-data-engine\\personal-data-engine', 'io_config.yaml')
    config_profile = 'default'

    try:
        # Intentamos conectar con Snowflake usando la configuraci�n
        with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
            # Solo probamos la conexi�n sin hacer ninguna operaci�n
            print("Conexi�n a Snowflake exitosa")
            return True
    except Exception as e:
        print(f"Error al conectar con Snowflake: {e}")
        return False

# Ejecutamos la funci�n para verificar la conexi�n
test_snowflake_connection()
