from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

class TelaInicial(MDScreen):
    
    def conhecer(self):
        print("Clicado")
        pass

    def logar(self):
        self.manager.current = 'login'
        print("Clicado")
        pass
