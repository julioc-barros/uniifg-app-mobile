from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

class Tela_Menu_Principal(MDScreen):
    
    def btn_atendimento(self):
        self.manager.current = 'tela_menu_atendimento'
        pass
    
    def btn_disciplinas(self):
        print("btn_disciplinas")
        pass
    
    def btn_acessos(self):
        print("btn_acessos")
        pass
    
    def btn_meucurso(self):
        print("btn_meucurso")
        pass
    
    def btn_solicitacoes(self):
        print("btn_solicitacoes")
        pass
    
    def btn_instalacoes(self):
        print("btn_instalacoes")
        pass
    
    def btn_financeiro(self):
        print("btn_financeiro")
        pass
    
    def btn_negociacao(self):
        print("btn_negociacao")
        pass
    
    def btn_outrasinfo(self):
        pass
    
    def voltar(self):
        self.manager.current = 'inicio'
        pass