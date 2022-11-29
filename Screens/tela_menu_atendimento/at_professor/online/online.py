from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import webbrowser

class Tela_Menu_At_Professor_Online(MDScreen):

    def voltar(self):
        self.manager.current = 'tela_menu_atendimento_at_professor'
    