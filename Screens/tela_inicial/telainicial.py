from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import webbrowser

class TelaInicial(MDScreen):
    
    def conhecer(self):
        webbrowser.open("https://www.unifg.edu.br/")

    def logar(self):
        self.manager.current = 'login'
        
