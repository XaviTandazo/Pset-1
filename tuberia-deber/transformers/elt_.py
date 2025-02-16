from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.mysql import MySQL
from mage_ai.io.snowflake import Snowflake
from os import path
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


# **1. Extraer datos desde RAW**
@data_loader
def load_data_from_mysql(*args, **kwargs):
    config_path = path.join('C:\\Users\\Paul Tandazo\\Documents\\deber1-data\\personal-data-engine\\personal-data-engine', 'io_config.yaml')
    config_profile = 'default'

    query = 'SELECT * FROM instacart_orders'  # Se puede modificar para cada tabla
    
    with MySQL.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        return loader.load(query)


# **2. Transformar los datos según el plan de acción del EDA**
@transformer
def transform_data(df, *args, **kwargs):
    # **Manejo de valores nulos**
    df['days_since_prior_order'].fillna(df['days_since_prior_order'].median(), inplace=True)

    # **Eliminar duplicados**
    df.drop_duplicates(inplace=True)

    # **Conversión de tipos de datos**
    df['order_id'] = df['order_id'].astype(int)
    df['user_id'] = df['user_id'].astype(int)
    df['order_number'] = df['order_number'].astype(int)
    df['order_dow'] = df['order_dow'].astype(int)
    df['order_hour_of_day'] = df['order_hour_of_day'].astype(int)

    # **Generar columnas derivadas**
    df['order_hour_category'] = pd.cut(df['order_hour_of_day'], bins=[0, 6, 12, 18, 24], labels=['Noche', 'Mañana', 'Tarde', 'Noche'])

    # **Devolver DataFrame transformado**
    return df


# **3. Cargar los datos limpios en Snowflake en el esquema CLEAN**
@data_exporter
def export_data_to_snowflake(df, *args, **kwargs):
    config_path = path.join('C:\\Users\\Paul Tandazo\\Documents\\deber1-data\\personal-data-engine\\personal-data-engine', 'io_config.yaml')
    config_profile = 'default'

    table_name = 'fact_orders_clean'

    with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(df, table_name, if_exists='replace')