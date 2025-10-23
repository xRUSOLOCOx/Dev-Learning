import re


regular_expressions = {
     
    "email": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
    "password": r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#$%^&+=!¡¿?._-]{8,}$",
    "full_name": r"^[A-Za-zÀ-ÖØ-öø-ÿ' \-]{10,60}$",
    "username": r"^[A-Za-z0-9_]{6,20}$",
    "age": r"^(?:120|11[0-9]|10[0-9]|[1-9]?[0-9])$",

}



def user_sign_up_menu():


# Ejemplo 2: TODO INCORRECTO (nombre muy corto, usuario con espacios, edad no numerica, email mal, password sin mayus/digito)
# sample_all_incorrect = {
#     'full_name': "Ana",
#     'user_name': "usuario con espacios",
#     'age': "-5",
#     'email': "correo@invalido",
#     'password': "password"
#}

    # Variables de almacenamiento de datos del usuario:

    full_name = "Ana"
    user_name = "ana suares "
    age = "-5"
    email = "correo@invalido"
    password = "password"


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
        
        print("Error al validar datos:")

        for linea_error in errors:
            print("-", linea_error)
    
    else:

        # Retorno de datos del usuario validados:

        user_data = {

            "fullname": full_name,
            "user_name": user_name,
            "age":age,
            "email":email,
            "password":password
        }

        return user_data


# Si quieres ejecutar interactivamente, descomenta la siguiente línea:














# Variables Fijas para test de funcion de validacion:

# Ejemplo 1: TODO CORRECTO
# sample_all_correct = {
#     'full_name': "Ana María Pérez López",
#     'user_name': "ana_perez01",
#     'age': "34",
#     'email': "ana.perez@example.com",
#     'password': "Password1"
#}


# Ejemplo 3: MIXTO (algunos campos correctos, otros no)
# sample_mixed = {
#     'full_name': "Luis Gonzalez",
#     'user_name': "luisg",
#     'age': "150",               # fuera de rango
#     'email': "luis.gonzalez@mail.com",
#     'password': "nopass"         # no cumple (sin mayúscula/dígito/long)
#}

# Uso: importar la función de validación y pasar los dicts (descomentar y ejecutar):
# from validacion import user_sign_up_validate_data
# print(user_sign_up_validate_data(**sample_all_correct))



