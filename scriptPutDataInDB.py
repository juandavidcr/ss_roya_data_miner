#!/usr/bin/env python

import mysql.connector
import pandas as pd

def insert_data_from_text_file(file_path, db_config, table_name):
    # Leer el archivo de texto usando pandas
    df = pd.read_csv(file_path, delimiter='\t')  # Cambiar el delimitador si es necesario

    # Conectar a la base de datos MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Insertar cada fila del DataFrame en la tabla
        for _, row in df.iterrows():
            data = tuple(row)  # Convertir la fila del DataFrame en una tupla para la inserción
            placeholders = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(query, data)
        
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        print("Datos insertados correctamente en la base de datos.")
    except mysql.connector.Error as err:
        print(f"Error al insertar los datos: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    # Configuración de la base de datos
    db_config = {
        "host": "localhost",
        "user": "tu_usuario",
        "password": "tu_contraseña",
        "database": "nombre_base_de_datos"
    }

    # Nombre de la tabla donde se insertarán los datos
    table_name = "nombre_tabla"

    # Ruta del archivo de texto
    file_path = "ruta/del/archivo.txt"

    insert_data_from_text_file(file_path, db_config, table_name)