from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

class Tela_Menu_Atendimento(MDScreen):

    def btn_at_caa (self):
        self.manager.current = 'tela_menu_atendimento_at_caa'

    def btn_at_coordenação (self):
        self.manager.current = 'tela_menu_atendimento_at_coordenacao'

    def btn_at_cac (self):
        self.manager.current = 'tela_menu_atendimento_at_cac'

    def btn_at_biblioteca (self):
        self.manager.current = 'tela_menu_atendimento_at_biblioteca'

    def btn_at_Agendamento (self):
        self.manager.current = 'tela_menu_atendimento_at_agendamento'

    def btn_at_carreiras (self):
        self.manager.current = 'tela_menu_atendimento_at_carreiras'

    def btn_at_professor (self):
        self.manager.current = 'tela_menu_atendimento_at_professor'

    def btn_at_sms_ligacao (self):
        self.manager.current = 'tela_menu_atendimento_sms_ligacao'

    def voltar(self):
        self.manager.current = 'login'
        pass