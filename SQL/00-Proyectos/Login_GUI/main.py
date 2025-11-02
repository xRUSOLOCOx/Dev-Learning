import flet as ft
from components import Login_Components

class MAIN_APP:

    def main(self,page:ft.Page):


        # Configuracion basica de ventana principal del sistema:

        page.title = "LOGIN_GUI"
        page.window.width = 1150
        page.window.height = 730

        page.window.resizable = False
        page.window.maximizable = False

        page.padding = 0
        page.spacing = 0

        page.bgcolor = "#11212d"

        # Componente de ventana principal:

        content_component = Login_Components.COMPONENTS.content_component
        nav_component = Login_Components.COMPONENTS.nav_component


        page.add(ft.Column(

            [
                ft.Container(

                    bgcolor="#11212d",
                    padding=ft.padding.only(left=10),
                    border=ft.Border(
                    bottom=ft.BorderSide(2, color="white")
                       
                    ),

                    content = ft.Row(

                        [

                            ft.Text(value= "LOGIN_GUI",color="white",size=45),
                            ft.Image(src= r"SQL/00-Proyectos/Login_GUI/assets/icon.jpg",width=120,height=100)

                        ],
                        
                        alignment= ft.MainAxisAlignment.SPACE_BETWEEN

                    ),

                ),

                ft.Container(

                    bgcolor="#1B1D1E",
                    content= ft.Row(

                        [

                            ft.Container(

                                bgcolor="gray",
                                content=content_component(),
                                expand=4,
                                padding=ft.padding.only(left=10) 
                                
                                
                            ),


                            ft.Container(


                                content=nav_component(),  
                                expand=1,
                                alignment=ft.alignment.center_right,
                                padding=ft.padding.only(right=13,top=20)
                            )
                        ],

                        vertical_alignment=ft.CrossAxisAlignment.START
                        
                    ),

                    padding=ft.padding.only(top=20)
                    
                )
            ],

            spacing=0
           
        )

        )

        

if __name__ == "__main__":
    app = MAIN_APP()
    ft.app(app.main)