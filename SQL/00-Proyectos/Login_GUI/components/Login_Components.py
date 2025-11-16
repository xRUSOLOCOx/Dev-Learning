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
            scroll="always"
            

        ),

        padding=ft.padding.only(left=10,top=40,right=20),
        
        
        )
    

    
    def nav_component(show_sign_in,show_sign_up,show_admin_sign_in,quit_app):
        
        return ft.Container(


            content=ft.Column(

            [

                ft.Button(
                    
                    text="Sign User In",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="green"),padding=ft.padding.only(top=20,bottom=20)),
                    color="green",
                    on_click=show_sign_in
                    
                    ),


                ft.Button(

                    text="Sign Admin In",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="green"),padding=ft.padding.only(top=20,bottom=20)),
                    color="green",
                    on_click=show_admin_sign_in
                    
                

                    ),

                ft.Button(

                    text="Sign User Up",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="blue"),padding=ft.padding.only(top=20,bottom=20)),
                    color="blue",
                    on_click=show_sign_up


                    ),

                ft.Container(


                    content= ft.Button(

                    text="Quit System",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="red"),padding=ft.padding.only(top=20,bottom=20)),
                    color="red",
                    on_click=quit_app

                    ),

                    margin=ft.margin.only(top=150),
                    
                )

            ],

            spacing=50,   
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,


        ),

        padding=ft.padding.only(left=10,top=40,right=10)

        )

    def sign_in_component(data_print_event):
        
        

        return ft.Container(
            
            
            content= ft.Column(

            [

                # Controles principales de componente sign in:

                ft.Text(value="INICIO DE SESIÓN USUARIO",size=30,weight=ft.FontWeight.BOLD),
                ft.TextField(label="Correo",width=550,border_color="white"),
                ft.TextField(label="Contraseña",width=550,border_color="white"),

                # Boton de envio de datos:

                ft.Button(text="ENTRAR",on_click= data_print_event,width=550,bgcolor="green",color="black",style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(10))),


                ft.Row(
                    
                    [
                        
                        ft.Text(spans=[ft.TextSpan(text="¿olvidaste tu contraseña?")],color="#09C1FF"),
                        ft.Text(spans=[ft.TextSpan(text="!Registrate Aqui¡")],color="#09C1FF")
                     
                     ],
                    
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                    
                    ),
  
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            height=600,
            
        ),

        padding=ft.padding.only(top=70),
        
                                                                             
        )
    
    def sign_up_component():
        
        return ft.Container(
            
            
            content= ft.Column(

            [

                # Controles principales de componente sign in:

                ft.Text(value="CREA TU CUENTA USUARIO",size=30,weight=ft.FontWeight.BOLD),
                

                ft.Row(

                    
                    [
                        
                        ft.TextField(label="Nombre",border_color="white",width=265),
                        ft.TextField(label="Edad",border_color="white",width=265),

                     
                     ],
                    
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20

                

                ),


                    ft.TextField(label="Correo",width=550,border_color="white"),
                    ft.TextField(label="Contraseña",width=550,border_color="white"),


                # Boton de envio de datos:

                ft.Button(text="ENTRAR",width=550,bgcolor="green",color="black",style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(10))),


                ft.Row(
                    
                    [
                        
                        ft.Text(spans=[ft.TextSpan(text="¿Ya tienes cuenta?")],color="#09C1FF"),
                        ft.Text(spans=[ft.TextSpan(text="Terminos y condiciones")],color="#09C1FF")
                     
                     ],
                    
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                    
                    ),
  
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            height=600,
            
        ),

        padding=ft.padding.only(top=60),
        
                                                                             
        )

    
    def sing_admin_component():

        return ft.Container(
            
            
            content= ft.Column(

            [

                # Controles principales de componente sign in:

                ft.Text(value="INICIO DE SESIÓN ADMIN",size=30,weight=ft.FontWeight.BOLD),
                ft.TextField(label="Correo",width=550,border_color="white"),
                ft.TextField(label="Contraseña",width=550,border_color="white"),

                # Boton de envio de datos:

                ft.Button(text="ENTRAR",on_click= "",width=550,bgcolor="green",color="black",style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(10))),


                ft.Text(spans=[ft.TextSpan(text="¿olvidaste tu contraseña?")],color="#09C1FF"),
  
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            height=600,
            
        ),

        padding=ft.padding.only(top=70),
        
                                                                             
        )


    def modal_quit_app_window(handle_action_click):


        cupertino_actions = [

            ft.CupertinoDialogAction(

                "SI",
                is_destructive_action=True,
                on_click=handle_action_click,
            ),
            
            ft.CupertinoDialogAction(

                text="NO",
                is_default_action=False,
                on_click=handle_action_click,

            ),
        ]


        return ft.CupertinoAlertDialog(

            title=ft.Text("Alerta del sistema"),
            content=ft.Text("Estas seguro de salir?"),
            actions=cupertino_actions,
            modal=True


        )