from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

class Tela_Menu_Atendimento(MDScreen):

    def btn_at_caa (self):
        self.manager.current = 'tela_menu_atendimento_at_caa'

    def btn_at_coordenação (self):
        pass

    def btn_at_cac (self):
        self.manager.current = 'tela_menu_atendimento_at_cac'

    def btn_at_biblioteca (self):
        pass

    def btn_at_Agendamento (self):
        pass

    def btn_at_carreiras (self):
        pass

    def btn_at_professor (self):
        pass

    def btn_at_sms_ligacao (self):
        pass

    def voltar(self):
        self.manager.current = 'tela_menu_principal'
        pass