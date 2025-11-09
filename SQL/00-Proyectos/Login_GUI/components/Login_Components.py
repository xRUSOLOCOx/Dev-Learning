import flet as ft
from views import messages_repository
from services import event_handlers


class COMPONENTS:

    def content_component():

        return ft.Container(

            content=ft.Column(

            [

                ft.Container(


                    content = ft.Column(
                        
                        [

                            ft.Text(value="PROYECTO LOGIN_GUI",size=25,weight=ft.FontWeight.BOLD),
                            ft.Text(value=event_handlers.EVENTS_HANDLERS.text_config(messages_repository.PROJECT_INTRODUCTION),size=18,text_align=ft.TextAlign.JUSTIFY),

                        ]
                    
                    )

                ),

                ft.Container(


                    content=ft.Column(


                        [

                            ft.Text(value="INSTRUCCIONES",size=25,weight=ft.FontWeight.BOLD),
                            ft.Text(value=messages_repository.PROJECT_INSTRUCTIONS,size=18,text_align=ft.TextAlign.JUSTIFY),

                        ]
                    )
                )

                
            ],

            spacing=40,
            height=510,
            scroll="auto"
            

        ),

        padding=ft.padding.only(left=10,top=40,right=20),
        
        

        )
    

    
    def nav_component():

        return ft.Container(


            content=ft.Column(

            [

                ft.Button(
                    
                    text="Sign User In",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="green"),padding=ft.padding.only(top=20,bottom=20)),
                    color="green"
                    
                    ),


                ft.Button(

                    text="Sign Admin In",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="green"),padding=ft.padding.only(top=20,bottom=20)),
                    color="green",
                    

                    ),

                ft.Button(

                    text="Sign User Up",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="blue"),padding=ft.padding.only(top=20,bottom=20)),
                    color="blue"

                    ),

                ft.Container(


                    content= ft.Button(

                    text="Quit System",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="red"),padding=ft.padding.only(top=20,bottom=20)),
                    color="red"

                    ),

                    margin=ft.margin.only(top=150),
                    
                )

            ],

            spacing=50,   
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,


        ),

        padding=ft.padding.only(left=10,top=40,right=10)

        )

    def sign_in_component(self):
        
        return ft.Text(value="hola mundo")

    def sign_up_component(self):
        pass
    
    def sing_admin_component(self):
        pass
    


# if __name__ == "__Login_Components__":

#     app = COMPONENTS
#     ft.app(target = app.content_component)