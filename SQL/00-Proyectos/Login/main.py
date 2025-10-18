# Archivo: main.py
# Lógica principal del programa de login y orquestación de flujo.

from text import WELCOME_USER
from validacion import user_option_menu_access


def user_option_menu():

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


    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    name = input("Ingrese su nombre completo: ")
    age = input("Ingrese su edad: ")
    email = input("Ingrese su correo: ")
    




def run_app():

    print(WELCOME_USER)

    while True:
        
        option = user_option_menu_access()

        if option == 1:

            print("opcion 1")


        elif option == 2:

            print("opcion 2")


        elif option == 3:

            print("opcion 3")


        elif option == 4:

            print("Adios")
            break

run_app()