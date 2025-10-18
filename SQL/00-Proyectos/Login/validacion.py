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

}

def user_option_menu_access():

    try:

        valid_options = (1,2,3,4)

        option = int(input("Ingrese valor numerico de 1 a 3 de las opciones disponibles: "))

        if option not in valid_options:

            print(f"Error: Ingreso de una opcion no valida {option}")

            return False
        
        else:

            return option

    except:

        print(f"Error: Usted ha ingresado un valor incorrecto.")

def user_sign_in_menu():



    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")



def user_sign_up_menu():

    user_data_input = {

        
        "full_name":input("Ingrese su nombre completo: "),
        "age":input("Ingrese su edad: "),
        "username":input("Ingrese su nombre de usuario: "),
        "password":input("Ingrese su contraseña: "),
        "email":input("Ingrese su correo: ")

    }
    # Strip inputs and validate using helper functions
    full_name = user_data_input["full_name"].strip()
    age = user_data_input["age"].strip()
    username = user_data_input["username"].strip()
    password = user_data_input["password"]
    email = user_data_input["email"].strip()

    errors = []
    if not valid_full_name(full_name):
        errors.append("Nombre completo inválido. Usa solo letras, espacios y guiones (10-60 caracteres).")
    if not valid_age(age):
        errors.append("Edad inválida. Debe ser un número entre 0 y 120.")
    if not valid_username(username):
        errors.append("Nombre de usuario inválido. 4-20 caracteres; letras, números y guión bajo.")
    if not valid_password(password):
        errors.append("Contraseña inválida. Mínimo 8 caracteres, al menos una mayúscula y un dígito.")
    if not valid_email(email):
        errors.append("Correo electrónico inválido.")

    if not errors:
        print("pasas amigo")
    else:
        print("Error al validar datos:")
        for e in errors:
            print(" - ", e)


user_sign_up_menu()







