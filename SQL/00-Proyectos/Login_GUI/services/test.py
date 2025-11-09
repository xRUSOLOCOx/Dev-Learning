# import flet as ft
# import test_2   

# def main(page: ft.Page):
    

#     def mostrar_hola_mundo(e):

#         contentenedor_1 = test_2.componentes.contenedor_1()
#         contenedor_principal.content = contentenedor_1

#         page.update()

#     def mostrar_hello_world(e):

#         contentenedor_2 = test_2.componentes.contenedor_2()
#         contenedor_principal.content = contentenedor_2

#         page.update()


#     # Componentes:


#     contenedor_principal = ft.Container(content=ft.Text(value="Hola soy una cadena"))

#     page.add(
        
#         ft.Column(

#             [
#                 ft.Container(content = contenedor_principal),
#                 ft.Button(text="presioname para ver tu hola mundo",on_click=mostrar_hola_mundo),
#                 ft.Button(text="presioname para ver tu hello world",on_click=mostrar_hello_world)

#             ]

#         )

#         )

# ft.app(main)


# # on_click=mostrar_hola_mundo(contenedor_1)
# # on_click=mostrar_hello_world(contenedor_2)