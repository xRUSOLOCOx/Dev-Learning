from components import Login_Components
import flet as ft


class EVENTS_HANDLERS:

    def __init__(self):
        
        self.page = ft.Page

    def text_config(value:str):

        return value.replace("\n"," ").strip()
