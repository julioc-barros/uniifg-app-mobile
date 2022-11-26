from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import webbrowser

class Tela_Menu_At_CAA(MDScreen):

    def whatsapp (self):
        webbrowser.open("https://api.whatsapp.com/send?phone=5581934615556&text=%2B55%2081%203461-5556")

    def voltar(self):
        self.manager.current = 'tela_menu_atendimento'
        