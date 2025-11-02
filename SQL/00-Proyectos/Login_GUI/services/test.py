import flet as ft

def main(page: ft.Page):
    page.title = "Login / Registro dinámico"
    page.window.width = 400
    page.window.height = 400
    page.window.center()

    # --- FUNCIONES ---
    def mostrar_registro(e):
        contenedor_principal.content = formulario_registro
        page.update()

    def mostrar_login(e):
        contenedor_principal.content = formulario_login
        page.update()

    # --- FORMULARIO DE LOGIN ---
    formulario_login = ft.Column(
        [
            ft.Text("Iniciar sesión", size=25, weight="bold"),
            ft.TextField(label="Correo electrónico", width=300),
            ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300),
            ft.ElevatedButton("Entrar", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
            ft.TextButton("¿No tienes cuenta? Regístrate", on_click=mostrar_registro),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # --- FORMULARIO DE REGISTRO ---
    formulario_registro = ft.Column(
        [
            ft.Text("Crear cuenta", size=25, weight="bold"),
            ft.TextField(label="Nombre completo", width=300),
            ft.TextField(label="Correo electrónico", width=300),
            ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300),
            ft.TextField(label="Confirmar contraseña", password=True, can_reveal_password=True, width=300),
            ft.ElevatedButton("Registrarme", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
            ft.TextButton("¿Ya tienes cuenta? Inicia sesión", on_click=mostrar_login),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # --- CONTENEDOR PRINCIPAL (comienza con el login) ---
    contenedor_principal = ft.Container(
        content=formulario_login,
        alignment=ft.alignment.center
    )

    # Agregar al layout
    page.add(contenedor_principal)

ft.app(target=main)
