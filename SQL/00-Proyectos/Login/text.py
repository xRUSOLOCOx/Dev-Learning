# text.py - Repositorio de texto y documentación

# Responsabilidades:

# - Almacenar constantes de texto usadas en notebooks y scripts.
# - Mantener descripciones de conceptos y ejemplos reutilizables.
# - No ejecutar lógica; sólo datos textuales que pueden ser importados.


WELCOME_USER_SIGNUP =  """

---------------------------------------------------------------------------------------------------------------------------

    BIENVENIDO USUARIO — FORMULARIO DE REGISTRO E INSTRUCCIONES:

    Reglas de validación (por favor úsalas al completar los campos):


        - Nombre de usuario: 6-20 caracteres; solo letras, números y guión bajo (_); sin espacios.
        Ejemplo: usuario_01

        - Contraseña: mínimo 8 caracteres; debe incluir al menos una letra MAYÚSCULA y al menos un dígito.
        Puede contener símbolos comunes (@ # $ % ^ & + = ! ¿ ? . _ -).
  
        - Nombre completo: solo letras (acepta acentos), espacios, guiones y apóstrofes; máximo 60 caracteres.
 
        - Edad: número entero entre 0 y 120.

        - Correo: formato estándar.

        Completa cada campo siguiendo estas reglas para que la validación sea exitosa.

---------------------------------------------------------------------------------------------------------------------------

"""

WELCOME_USER = """

---------------------------------------------------------------------------------------------------------------------------

    BIENVENIDO USUARIO — SELECCIONE UN NUMERO DE LAS OPCIONES DISPONIBLES:

    1. Inicio sesión usuario.
    2. Inicio sesión administrador.
    3. registrar usuario.
    4. Salir del sistema.

---------------------------------------------------------------------------------------------------------------------------

"""

WELCOME_USER_SIGNIN = """

---------------------------------------------------------------------------------------------------------------------------

    BIENVENIDO USUARIO, Por favor ingrese sus credenciales para iniciar sesion.


    - Nombre de usuario: 6-20 caracteres; solo letras, números y guión bajo (_); sin espacios.
        Ejemplo: usuario_01

    - Contraseña: mínimo 8 caracteres; debe incluir al menos una letra MAYÚSCULA y al menos un dígito.
        Puede contener símbolos comunes (@ # $ % ^ & + = ! ¿ ? . _ -).

---------------------------------------------------------------------------------------------------------------------------

"""

USER_MENU = """

---------------------------------------------------------------------------------------------------------------------------

    BIENVENIDO USUARIO — SELECCIONE UN NUMERO DE LAS OPCIONES DISPONIBLES:

    1. Cambiar contraseña.
    2. Eliminar cuenta.
    3. Cerrar sesión.

---------------------------------------------------------------------------------------------------------------------------

"""


MODIFY_PASSWORD = """

---------------------------------------------------------------------------------------------------------------------------

    PARA INGRESAR LA NUEVA CONTRASEÑA TENGA EN CUENTA LAS INSTRUCCIONES:

    - Contraseña: mínimo 8 caracteres; debe incluir al menos una letra MAYÚSCULA y al menos un dígito.
        Puede contener símbolos comunes (@ # $ % ^ & + = ! ¿ ? . _ -).
        
---------------------------------------------------------------------------------------------------------------------------        

"""

DELETE_USER = "!ELIMINANDO CUENTA¡"