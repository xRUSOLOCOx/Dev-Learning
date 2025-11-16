import flet as ft


def main(page:ft.Page):

    correo = ft.TextField(label="Correo")
    contrasena = ft.TextField(label="Contraseña", password=True)

    def entrar(e):
        
        if not correo.value:
            correo.error_text = "El correo no puede estar vacío"
        if not contrasena.value:
            contrasena.error_text = "La contraseña es obligatoria"

        correo.update()
        contrasena.update()

    page.add(
        correo,
        contrasena,
        ft.ElevatedButton("Entrar", on_click=entrar)
    )

ft.app(main)