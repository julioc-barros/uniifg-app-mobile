from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import webbrowser

class Tela_Menu_At_CAC(MDScreen):

    def btn_at_cac_unidades(self):
        pass
    
    def btn_at_cac_contato(self):
        pass
    
    def btn_at_cac_ingresso(self):
        pass
    

    def voltar(self):
        self.manager.current = 'tela_menu_atendimento'
        