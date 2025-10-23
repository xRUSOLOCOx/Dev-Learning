# Archivo: main.py
# Lógica principal del programa de login y orquestación de flujo.

from text import WELCOME_USER,WELCOME_USER_SIGNUP,WELCOME_USER_SIGNIN,USER_MENU,MODIFY_PASSWORD
from validacion import main_menu, user_sign_up_menu,user_sign_in_menu,user_option_menu_access,password_validation
from conexion import register_user,sing_user_in,modify_password,delete_user


def run_app():

    close_first_loop = []
    while len(close_first_loop) == 0:

        print(WELCOME_USER)

        close_second_loop = []
        while len(close_second_loop) == 0:
            
            option = main_menu()

            if option == 1:

                print(WELCOME_USER_SIGNIN)
                
                validation = user_sign_in_menu()

                if not validation:

                    print("\nError: No se ha podido continuar con el inicio de sesión, !Tenga en cuenta las instrucciones de inicio!")
                    break

                else:
                    
                    sing_validation = sing_user_in(validation)

                    if not sing_validation:

                        print("Error: Usuario o contraseña incorrectas")

                        break

                    else:
                        
                        while True:

                            print(f"\nIniciaste sesion {validation["username"]}\n{USER_MENU}")

                            option = user_option_menu_access()

                            if option == 1:

                                print(MODIFY_PASSWORD)
                                validation = password_validation()

                                if not validation:

                                    print("\nError: Formato de contraseña incorrecto!")
                                    
                                else:

                                    modify_password(sing_validation,validation)
                                    print("\nCONTRASEÑA CAMBIADA EXITOSAMENTE. Inicie sesión de nuevo.")

                                    close_second_loop.append(1)
                                    break
                                    
                                    

                            elif option == 2:

                                print(sing_validation)

                                if delete_user(sing_validation):

                                    print("Cuenta eliminada")
                                    close_second_loop.append(1)
                                    break
                                    

                            elif option == 3:

                                close_second_loop.append(1)
                                break

            elif option == 2:

                print("opcion 2")


            elif option == 3:

                print(WELCOME_USER_SIGNUP)
                validation = user_sign_up_menu()

                if not validation:

                    print("\nError: No se ha podido registrar el usuario, !Tenga en cuenta las instrucciones de registro!")
                    break

                else:

                    register_user(validation)
                    break
        

            elif option == 4:

                print("Adios")
                close_first_loop.append(1)

                break



run_app()