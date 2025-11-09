import flet as ft
from views import messages_repository
from components import Login_Components

class MAIN_APP:

    def main(self,page:ft.Page):


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

        # Componente de ventana principal:

        main_component = Login_Components.COMPONENTS.content_component()




        page.add(ft.Column(

            [
                ft.Container(

                    content = ft.Row(

                        [

                            ft.Text(value="LOGIN_GUI",size=45,weight=ft.FontWeight.BOLD),
                            ft.Image(src="assets/icon.jpg",width=80,height=80)

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

                                content=Login_Components.COMPONENTS.nav_component(),
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
        )

        

if __name__ == "__main__":
    app = MAIN_APP()
    ft.app(app.main)