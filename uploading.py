import pandas as pd
import numpy as np
import psycopg2

TYPES_TO_SQL = {
    "object": "TEXT",
    "int64": "INTEGER",
    "float64": "REAL",
    "datetime64[ns]": "TEXT",
}

def change_column_names(df):
    df.columns = df.columns.str.replace(" ", "__")
    df.columns = df.columns.str.replace(".", "")
    df.columns = df.columns.str.replace("=", "_")
    return df

def sql_command_create_table(df, table_name):
    cols = df.columns
    cols_types = df.dtypes
    sql_create_table = f"CREATE TABLE {table_name} (\n"

    for col, dtype in zip(cols, cols_types):
        sql_type = TYPES_TO_SQL[str(dtype)]
        sql_create_table += f"    {col} {sql_type},\n"

    sql_create_table = sql_create_table.rstrip(",\n") + "\n);"

    return sql_create_table

# Datos de conexión de Supabase
host = "aws-0-us-east-1.pooler.supabase.com"
user = "postgres.bfpvgfrvcwmresxlsium"
password = "jExls2hLZ0Wvyjbt"
dbname = "postgres"

# Conectar a la base de datos PostgreSQL en Supabase
conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    dbname=dbname
)
cursor = conn.cursor()

print("Conectado a Supabase.")

# Leemos los datos de los hospitales
df_hospital1 = pd.read_excel("data/hospital1.xlsx")
df_hospital2 = pd.read_excel("data/hospital2.xlsx")

# Cambiar los nombres de las columnas
df_hospital1 = change_column_names(df_hospital1)
df_hospital2 = change_column_names(df_hospital2)

# Cambiar los tipos de datos para compatibilidad con PostgreSQL
df_hospital2['date_of_first_symptoms'] = df_hospital2['date_of_first_symptoms'].astype(object).where(df_hospital2['date_of_first_symptoms'].notnull(), np.nan)
df_hospital2['admission_date'] = df_hospital2['admission_date'].astype(object).where(df_hospital2['admission_date'].notnull(), np.nan)

# Reemplazar NaN en columnas numéricas antes de convertir a int64
df_hospital2['patient_id'] = df_hospital2['patient_id'].fillna(-1).astype('int64')
df_hospital2['admission_id'] = df_hospital2['admission_id'].fillna(-1).astype('int64')

# Crear la tabla hospital1 en la base de datos
cursor.execute(sql_command_create_table(df_hospital1, "hospital1_data"))
cursor.execute(sql_command_create_table(df_hospital2, "hospital2_data"))

print("Tablas creadas en Supabase.")

# Insertar los datos de df_hospital1 en la tabla 'hospital1'
insert_query = f"INSERT INTO hospital1_data ({', '.join(df_hospital1.columns)}) VALUES ({', '.join(['%s'] * len(df_hospital1.columns))})"
cursor.executemany(insert_query, df_hospital1.values)

print("Datos de hospital1 subidos a Supabase.")

# Insertar los datos de df_hospital2 en la tabla 'hospital2'
insert_query = f"INSERT INTO hospital2_data ({', '.join(df_hospital2.columns)}) VALUES ({', '.join(['%s'] * len(df_hospital2.columns))})"
cursor.executemany(insert_query, df_hospital2.values)

print("Datos de hospital2 subidos a Supabase.")

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Datos subidos a Supabase.")