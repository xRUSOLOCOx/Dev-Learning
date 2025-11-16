import flet as ft
import test_2

def main(page: ft.Page):

    def mostrar_hola_mundo(e):
        nuevo = test_2.componentes.contenedor_1()
        cambiar_con_animacion(nuevo)

    def mostrar_hello_world(e):
        nuevo = test_2.componentes.contenedor_2()
        cambiar_con_animacion(nuevo)

    # ---- FUNCIÓN DE ANIMACIÓN ----
    def cambiar_con_animacion(nuevo_contenido):
        # Guardamos el nuevo contenido
        contenedor_principal.data = nuevo_contenido
        
        # Fade-out
        contenedor_principal.opacity = 0
        contenedor_principal.update()

    # ---- Cuando termina la animación ----
    def fin_animacion(e):
        if contenedor_principal.opacity == 0:
            # Cambiamos texto aquí (después del fade)
            contenedor_principal.content = contenedor_principal.data
            # Fade-in
            contenedor_principal.opacity = 1
            contenedor_principal.update()

    # ---- CONTENEDOR PRINCIPAL ----
    contenedor_principal = ft.Container(
        content=ft.Text("Hola soy una cadena"),
        opacity=1,
        animate_opacity=ft.Animation(400, "ease"),
        on_animation_end=fin_animacion
    )

    page.add(
        ft.Column(
            [
                contenedor_principal,
                ft.Button("presioname para ver tu hola mundo", on_click=mostrar_hola_mundo),
                ft.Button("presioname para ver tu hello world", on_click=mostrar_hello_world),
            ]
        )
    )

ft.app(main)
