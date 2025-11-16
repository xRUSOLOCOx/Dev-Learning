import flet as ft
from views import messages_repository
from components import Login_Components
from services import event_handlers







class MAIN_APP:

    

    def main(self,page:ft.Page):


        # ------------------------------
        # APP PRINCIPAL
        # ------------------------------


        # Eventos de la aplicación:


        # Eventos de carga de componentes en la interfaz (Cambio dinamico del main_component contenedor principal):

        show_sign_in_event = lambda e:event_handlers.EVENTS_HANDLERS.show_sign_in_component(e,main_component,sign_in_component)
        show_main_event = lambda e:event_handlers.EVENTS_HANDLERS.show_main_component(e,main_component,content_component.content)
        show_sign_up_event = lambda e:event_handlers.EVENTS_HANDLERS.show_sign_up_component(e,main_component,sign_up_component)
        show_sign_in_admin_event = lambda e:event_handlers.EVENTS_HANDLERS.show_sign_up_component(e,main_component,sign_admin_in_component)


        # Eventos POST envio de datos de formulario:

        data_print_event = event_handlers.EVENTS_HANDLERS.data_print

        # Eventos de ventana modal y alertas:

        quit_app_event = lambda e:page.open(modal_quit)
        handle_action_click = lambda e:event_handlers.EVENTS_HANDLERS.handle_action_click(e,page)


        # Componentes de la aplicacion:

        main_component = Login_Components.COMPONENTS.content_component()
        content_component = Login_Components.COMPONENTS.content_component()
        sign_in_component = Login_Components.COMPONENTS.sign_in_component(data_print_event)
        sign_up_component = Login_Components.COMPONENTS.sign_up_component()
        nav_component = Login_Components.COMPONENTS.nav_component(show_sign_in_event,show_sign_up_event,show_sign_in_admin_event,quit_app_event)
        sign_admin_in_component = Login_Components.COMPONENTS.sing_admin_component()
        modal_quit = Login_Components.COMPONENTS.modal_quit_app_window(handle_action_click)
        

        

        # ------------------------------------------------------
        # CONFIGURACION BASICA DE VENTANA PRINCIPAL DEL SISTEMA:
        # ------------------------------------------------------


        # Configuracion basica de ventana principal del sistema:

        page.title = "LOGIN_GUI"
        page.padding = 0
        page.spacing = 0
        page.window.width = 1200
        page.window.height = 670
        page.window.min_width = 800
        page.window.min_height = 670
        page.window.max_width = 1200
        page.window.max_height = 670
        page.expand = False
        page.bgcolor = "#1b1d1e"


        # -------------------------------------------
        # INTERFAZ GUI DE LA APLICACION LOGIN_GUI
        # --------------------------------------------



        # Interfaz GUI de ventana principal:

        
        page.add(ft.Column(

            [
                ft.Container(

                    content = ft.Row(

                        [

                            ft.Text(
                                
                                
                                size=45,
                                weight=ft.FontWeight.BOLD,
                                spans=[ft.TextSpan(

                                    text="LOGIN_GUI",
                                    on_click=show_main_event


                                )]
                                
                                
                                ),

                            ft.Image(src="icon.jpg",width=80,height=80)

                        ],
                        
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),

                    padding=ft.padding.only(left=10,right=10),
                    border=ft.border.only(bottom=ft.BorderSide(1,"white")),
                    bgcolor="#11212d"

                ),

                ft.Container(


                    content=ft.Row(


                        [

                            ft.Container(

                                content=main_component,
                                expand=4,
                                border=ft.border.only(right=ft.BorderSide(1,"white")),
                                
                            ),


                            ft.Container(

                                content=nav_component,
                                expand=1,
                                
                                
                            )

                        ],

                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START


                    )



                )
  
            ],

            spacing=0
        )

        ),

    
        
    

        
if __name__ == "__main__":
    app = MAIN_APP()
    ft.app(app.main)