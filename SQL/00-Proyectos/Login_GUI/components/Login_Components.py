import flet as ft
from views import messages_repository

class COMPONENTS:

    def content_component():

        return ft.Column(

            [

                ft.Container(

                    content = ft.Column(

                        [
                            ft.Text(value="PROYECTO LOGIN_GUI",size=26,color="white",weight=ft.FontWeight.BOLD,font_family="OpenSans"),
                            ft.Text(value=messages_repository.PROJECT_INTRODUCTION,size=16,color="white"),
        
                        ],

                        spacing=0,
                        

                    )

                ),
                
                ft.Container(

                     content = ft.Column(

                        [
                            ft.Text(value="INSTRUCCIONES",size=26,color="white",weight=ft.FontWeight.BOLD,font_family="OpenSans"),
                            ft.Text(value=messages_repository.PROJECT_INSTRUCTIONS,size=16,color="white"),
        
                        ],

                        spacing=0,

                    )

                )

            ],

            spacing = 0

        )
    
    def nav_component():

        return ft.Column(

            [

                ft.FilledButton(
                    
                    content=ft.Text(

                        "Sign User In",color="#0d5c2c"

                        ),

                    bgcolor="white",

                    style=ft.ButtonStyle(

                        shape=ft.RoundedRectangleBorder(5),
                        side=ft.BorderSide(1,color="#0d5c2c")


                            ),

                    width=160,
                    height=50

                ),

                ft.FilledButton(
                    
                    content=ft.Text(

                        "Sign Admin in",color="#0d5c2c"

                        ),

                    bgcolor="white",

                    style=ft.ButtonStyle(

                        shape=ft.RoundedRectangleBorder(5),
                        side=ft.BorderSide(1,color="#0d5c2c")

                            ),

                    width=160,
                    height=50
                            
                ),

                ft.FilledButton(
                    
                    content=ft.Text(

                        "Sign User Up",color="#1f1d9d"

                        ),

                    bgcolor="white",

                    style=ft.ButtonStyle(

                        shape=ft.RoundedRectangleBorder(5),
                        side=ft.BorderSide(1,color="#1f1d9d")

                            ),

                    width=160,
                    height=50,
                            
                ),

                ft.Container(


                    content = ft.FilledButton(
                    
                    content=ft.Text(

                            "Quit App",color="Red"
                        ),

                    bgcolor="white",

                    style=ft.ButtonStyle(

                        shape=ft.RoundedRectangleBorder(5),
                        side=ft.BorderSide(1,color="Red")


                            ),

                    width=160,
                    height=50,
                    
                            
                ),

                margin= ft.margin.only(top=180)

                )
                
            ],

            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=40,
            
        )
        
    def sign_in_component(self):
        pass

    def sign_up_component(self):
        pass
    
    def sing_admin_component(self):
        pass
    


# if __name__ == "__Login_Components__":

#     app = COMPONENTS
#     ft.app(target = app.content_component)