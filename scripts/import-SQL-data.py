import os
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import yaml

# Ruta del archivo YAML
config_path = r"C:\Users\Paul Tandazo\Desktop\PSET1-datamining\tuberias-deber\io_config.yaml"

# Cargar credenciales desde el archivo YAML
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

# Extraer credenciales
host = config['default']['MYSQL_HOST']
port = config['default']['MYSQL_PORT']
user = config['default']['MYSQL_USER']
password = config['default']['MYSQL_PASSWORD']
database = config['default']['MYSQL_DATABASE']
SCHEMA = database

# Conexión con la base de datos
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

# Definir archivos
files = {
    r"C:\Users\Paul Tandazo\Desktop\PSET1-datamining\data\aisles.csv": "aisles",
    r"C:\Users\Paul Tandazo\Desktop\PSET1-datamining\data\departments.csv": "departments",
    r"C:\Users\Paul Tandazo\Desktop\PSET1-datamining\data\instacart_orders.csv": "instacart_orders",
    r"C:\Users\Paul Tandazo\Desktop\PSET1-datamining\data\order_products.csv": "order_products",
    r"C:\Users\Paul Tandazo\Desktop\PSET1-datamining\data\products.csv": "products"
}

# Nombres de las columnas según los archivos
column_names = {
    "aisles.csv": ["aisle_id", "aisle"],
    "departments.csv": ["department_id", "department"],
    "instacart_orders.csv": ["order_id", "user_id", "order_number", "order_dow", "order_hour_of_day", "days_since_prior_order"],
    "order_products.csv": ["order_id", "product_id", "add_to_cart_order", "reordered"],
    "products.csv": ["product_id", "product_name", "aisle_id", "department_id"]
}

# Cargar e insertar los datos
target_delimiter = ';'  # Ajustar el delimitador si es necesario
for file_path, table in files.items():
    if not os.path.exists(file_path):
        print(f"Error: El archivo {file_path} no existe. Verifica la ruta.")
        continue
    
    print(f"Importando {file_path} a la tabla {table}...")
    file_name = os.path.basename(file_path)
    df = pd.read_csv(file_path, delimiter=target_delimiter, names=column_names[file_name], header=0)
    df.to_sql(table, engine, schema=SCHEMA, if_exists='replace', index=False)
    print(f"{file_path} importado correctamente.")

print("Importación completada.")
