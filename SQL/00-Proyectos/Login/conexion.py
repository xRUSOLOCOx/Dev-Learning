# Archivo: validacion.py
# Flujo principal de conexion y consultas a base de datos.

import mysql.connector
from mysql.connector import Error


def database_connection():

    try:

        connection = mysql.connector.connect(
            
            user="root",
            password = "0000",
            database = "hello_mysql"
            
            )
        
        return connection
    
    except Error as main_error:

        return f"Error: {main_error}"
    