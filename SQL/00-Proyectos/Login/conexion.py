# Archivo: validacion.py
# Flujo principal de conexion y consultas a base de datos.

import mysql.connector
from mysql.connector import Error

# Funcion de conexion a la base de datos local:

def database_connection():

    try:

        connection = mysql.connector.connect(
            
            user="root",
            password = "0000",
            database = "login_project"
            
            )
         
        return connection
    
    except Error as main_error:

        return f"Error: {main_error}"


# Funcion de inserción de datos a la tabla usuarios:


def register_user(user_data_dict):

    connection = database_connection()
    cursor = connection.cursor()

    try:

        query = "INSERT INTO users (fullname,username,age,email,user_password) VALUES (%s,%s,%s,%s,%s)"
        user_data = (user_data_dict["fullname"],user_data_dict["user_name"],user_data_dict["age"],user_data_dict["email"],user_data_dict["password"])
        cursor.execute(query,user_data)
        connection.commit()
 
        print("Usuario Registrado correctamente.")

    except Error as insert_error:

        print(f"Error al registrar usuario: {insert_error}")


# Funcion de extracción de id y comparación de credenciales del usuario:

def sing_user_in(user_data_dict):

    connection = database_connection()
    cursor = connection.cursor()

    try:

        query = "SELECT user_id FROM users WHERE username = %s and user_password = %s"
        user_data = (user_data_dict["username"],user_data_dict["password"])
        cursor.execute(query,user_data)

        user_id = cursor.fetchone()[0]

        return {"user_id":user_id}

    except TypeError or Error as insert_error:

        return False

    finally:

        cursor.close()



def delete_user(user_data_dict):

    connection = database_connection()
    cursor = connection.cursor()

    try:

        query = "DELETE FROM users WHERE user_id = %s;"
        user_data = (user_data_dict["user_id"],)

        cursor.execute(query,user_data)
        connection.commit()

        return True

    except Error as insert_error:

        print(f"Error al eliminar cuenta: {insert_error}")

    finally:

        cursor.close()

def modify_password(user_id,user_data_dict):

    connection = database_connection()
    cursor = connection.cursor()

    try:

        query = "UPDATE users SET user_password = %s WHERE user_id = %s;"
        user_data = (user_data_dict["password"],user_id)

        cursor.execute(query,user_data)
        connection.commit()

        return True

    except Error as insert_error:

        print(f"Error al cambiar contraseña: {insert_error}")

    finally:

        cursor.close()