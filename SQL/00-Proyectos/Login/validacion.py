# """

# validacion.py

# Módulo de validaciones y consultas relacionadas con usuarios.

# Responsabilidades:
# - Contener expresiones regulares y funciones para validar campos de entrada
#     (email, username, password, name, age).
# - Proveer funciones auxiliares reutilizables por `main.py` u otros módulos.
# - Mantener las reglas de validación en un único lugar para facilitar pruebas.

# """


import re


regular_expressions = {
     
    "email": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
    "password": r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#$%^&+=!¡¿?._-]{8,}$",
    "full_name": r"^[A-Za-zÀ-ÖØ-öø-ÿ' \-]{10,60}$",
    "username": r"^[A-Za-z0-9_]{6,20}$",
    "age": r"^(?:120|11[0-9]|10[0-9]|[1-9]?[0-9])$",

}



# FUNCIONES DE NAVEGACIÓN POR EL SISTEMA:

def main_menu():

    try:

        valid_options = (1,2,3,4)

        option = int(input("Ingrese valor numerico de 1 a 4 de las opciones disponibles: "))

        if option not in valid_options:

            print(f"Error: Ingreso de una opcion no valida {option}")

            return False
        
        else:

            return option

    except:

        print(f"Error: Usted ha ingresado un valor incorrecto.")


def user_option_menu_access():

    try:

        valid_options = (1,2,3)

        option = int(input("Ingrese valor numerico de 1 a 3 de las opciones disponibles: "))

        if option not in valid_options:

            print(f"Error: Ingreso de una opcion no valida {option}")

            return False
        
        else:

            return option

    except:

        print(f"Error: Usted ha ingresado un valor incorrecto.")




# FUNCIONES DE VALIDACION DE ENTRADAS AL SISTEMA USANDO EXPRESIONES REGULARES:


def user_sign_in_menu():


    username = input("Ingrese su nombre de usuario: ").strip()
    password = input("Ingrese su contraseña: ").strip()

    errors = []

    if not re.fullmatch(regular_expressions["username"],username):
        errors.append("Error: Formato de Nombre usuario invalido.")

    if not re.fullmatch(regular_expressions["password"],password):
        errors.append("Error: Formato de Contraseña invalido.")

    if len(errors)>= 1:
        
        print("\nError al validar datos:\n")

        for linea_error in errors:
            print("-", linea_error)

    else:

        user_data = {

            "username": username,
            "password":password
        }

        return user_data



def user_sign_up_menu():


    # Variables de almacenamiento de datos del usuario:

    full_name = input("Ingrese su nombre completo: ")
    user_name = input("Ingrese su nombre de usuario: ").strip()
    age = input("Ingrese su edad: ").strip()
    email = input("Ingrese su correo electrinico: ").strip()
    password = input("Ingrese su contraseña: ").strip()


    # Validación de datos usando expresiones regulares:

    errors = []
    

    if not re.fullmatch(regular_expressions["full_name"],full_name):
        errors.append("Error: Nombre Invalido.")

    if not re.fullmatch(regular_expressions["username"],user_name):
        errors.append("Error: Nombre de usuario invalido.")

    if not re.fullmatch(regular_expressions["email"],email):
        errors.append("Error: Correo electronico invalido.")
    
    if not re.fullmatch(regular_expressions["age"],age):
        errors.append("Error: Edad ingresada invalida.")

    if not re.fullmatch(regular_expressions["password"],password):
        errors.append("Error: Contraseña ingresada invalida.")


    if len(errors)>= 1:
        
        print("\nError al validar datos:\n")

        for linea_error in errors:
            print("-", linea_error)
    
    else:

        # Retorno de datos del usuario validados:

        user_data = {

            "fullname": full_name,
            "user_name": user_name,
            "age":int(age),
            "email":email,
            "password":password
        }

        return user_data

def password_validation():

    password = input("Ingrese su nueva contraseña: ").strip()

    if not re.fullmatch(regular_expressions["password"],password):
        print("Error: Formato de Contraseña invalido.")

    else:

        user_data = {"password":password}

        return user_data







