from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import webbrowser

class Tela_Menu_At_Biblioteca(MDScreen):

    def btn_at_biblioteca_unidade(self):
        self.manager.current = "tela_menu_atendimento_at_biblioteca_unidade"

    def btn_at_biblioteca_cadastro(self):
        self.manager.current = "tela_menu_atendimento_at_biblioteca_cadastro"

    def btn_at_biblioteca_locacao(self):
        self.manager.current = "tela_menu_atendimento_at_biblioteca_locacao"

    def btn_at_biblioteca_multa(self):
        self.manager.current = "tela_menu_atendimento_at_biblioteca_multa"
        
    

    def voltar(self):
        self.manager.current = 'tela_menu_atendimento'
        