from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

class TelaLogin(MDScreen):

    def voltar(self):
        self.manager.current = 'inicio'

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if self.password.focus and keycode == 40:  # 40 - Enter key pressed
            self.auth()

    def auth(self):
        usuario = self.ids["'user'"].text
        senha = self.ids["'password'"].text
        
        if (usuario == 'admin') and (senha == 'admin'):
            self.ids["'user'"].text = ''
            self.ids["'password'"].text = ''
            self.manager.current = 'tela_menu_principal'
        else: 
            self.ids["'user'"].text = ''
            self.ids["'password'"].text = ''
            