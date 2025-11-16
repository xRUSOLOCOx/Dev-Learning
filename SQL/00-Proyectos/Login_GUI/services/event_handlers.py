


class EVENTS_HANDLERS:


    def text_config(value:str):

        return value.replace("\n"," ").strip()

    def handle_action_click(e,page):


        if e.control.text == "SI":

            page.window.destroy()

        else:
            page.close(e.control.parent)

    def data_print(e):

        user_email = e.control.parent.controls[1]
        user_password = e.control.parent.controls[2]

        if not user_email.value:

            user_email.error_text = "El correo no puede estar vacío"
            
            user_email.update()
            user_password.update()

        if not user_password.value:

            user_password.error_text = "La contraseña es obligatoria"

            user_email.update()
            user_password.update()

        
        
        
        print(user_email.value,user_password.value)


    def show_sign_in_component(e,main_component,new_component):

        main_component.content = new_component
        main_component.update()     

    def show_main_component(e,main_component,new_component): 
        
        main_component.content = new_component
        main_component.update()

    def show_sign_up_component(e,main_component,new_component): 
        
        main_component.content = new_component
        main_component.update()

    def show_sign_in_admin_component(e,main_component,new_component): 
        
        main_component.content = new_component
        main_component.update()

    def quit_app(e,page):

        page.window.destroy()