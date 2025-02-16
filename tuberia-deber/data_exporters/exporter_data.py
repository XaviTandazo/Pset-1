from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from os import path

def test_snowflake_connection():
    config_path = path.join('C:\\Users\\Paul Tandazo\\Documents\\deber1-data\\personal-data-engine\\personal-data-engine', 'io_config.yaml')
    config_profile = 'default'

    try:
        # Intentamos conectar con Snowflake usando la configuración
        with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
            # Solo probamos la conexión sin hacer ninguna operación
            print("Conexión a Snowflake exitosa")
            return True
    except Exception as e:
        print(f"Error al conectar con Snowflake: {e}")
        return False

# Ejecutamos la función para verificar la conexión
test_snowflake_connection()
