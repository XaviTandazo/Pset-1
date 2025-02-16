import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd

# Conexión a Snowflake
def connect_to_snowflake():
    try:
        # Configura la conexión a Snowflake
        conn = snowflake.connector.connect(
            user='XaviEr00396',
            password='Marshallmathers2000?',
            account='jw06674.mexico-central.azure',
            warehouse='DEBER1_DATA_MINNING_WH',
            database='DATABASE_DEBER1_DM_DB',
            schema='RAW',
            role='ACCOUNTADMIN'
        )
        print("Conexión exitosa a Snowflake")
        return conn
    except Exception as e:
        print(f"Error de conexión a Snowflake: {e}")
        return None

# Crear el esquema si no existe
def create_schema_if_not_exists(conn, schema_name, database):
    try:
        cursor = conn.cursor()
        
        # Definir la consulta SQL para crear el esquema si no existe
        create_schema_query = f"""
        CREATE SCHEMA IF NOT EXISTS {database}.{schema_name};
        """
        
        # Ejecutar la consulta
        cursor.execute(create_schema_query)
        print(f"Esquema {schema_name} verificado/creado exitosamente.")
    
    except Exception as e:
        print(f"Error al crear el esquema: {e}")

# Crear la tabla si no existe
def create_table_if_not_exists(conn, table_name, database, schema):
    try:
        cursor = conn.cursor()
        
        # Definir la consulta SQL para crear la tabla si no existe
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {database}.{schema}.{table_name} (
            product_id INT,
            product_name STRING,
            aisle_id INT,
            department_id INT
        );
        """
        
        # Ejecutar la consulta
        cursor.execute(create_table_query)
        print(f"Tabla {table_name} verificada/creada exitosamente.")
    
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

# Exportar datos a Snowflake
def export_data_to_snowflake(conn, df, table_name, database, schema):
    try:
        if conn is None:
            print("No se pudo conectar a Snowflake. Abortando operación.")
            return
        
        # Verifica las columnas del DataFrame
        print("Columnas del DataFrame a exportar:")
        print(df.columns)

        # Exporta los datos a Snowflake utilizando write_pandas
        write_pandas(conn, df, table_name, database=database, schema=schema)
        print(f"Datos exportados a {database}.{schema}.{table_name} correctamente.")
    
    except snowflake.connector.errors.ProgrammingError as e:
        print(f"Error de compilación SQL: {e}")
        print("Verifica la sintaxis de la consulta o la estructura de la tabla.")
    
    except Exception as e:
        print(f"Error inesperado durante la exportación de datos: {e}")

# Crear un DataFrame de ejemplo (simulando datos CSV)
data = {
    'product_id': [1, 2, 3, 4, 5, 6, 7],
    'product_name': ['Chocolate Sandwich Cookies', 'All-Seasons Salt', 'Robust Golden Unsweetened Oolong Tea',
                     'Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce', 'Green Chile Anytime Sauce',
                     'Dry Nose Oil', 'Pure Coconut Water With Orange'],
    'aisle_id': [61, 104, 94, 38, 5, 11, 98],
    'department_id': [19, 13, 7, 1, 13, 11, 7]
}
df = pd.DataFrame(data)

# Conectar a Snowflake y crear esquema y tabla si no existen
conn = connect_to_snowflake()
if conn:
    create_schema_if_not_exists(conn, 'RAW', 'DATABASE_DEBER1_DM_DB')
    create_table_if_not_exists(conn, 'products', 'DATABASE_DEBER1_DM_DB', 'RAW')
    export_data_to_snowflake(conn, df, 'products', 'DATABASE_DEBER1_DM_DB', 'RAW')
