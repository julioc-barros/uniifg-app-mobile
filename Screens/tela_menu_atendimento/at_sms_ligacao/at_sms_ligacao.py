from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import webbrowser

class Tela_Menu_At_Sms_Ligacao(MDScreen):

    def btn_at_sms_ligacao_soualuno(self):
        self.manager.current = 'tela_menu_atendimento_at_sms_ligacao_soualuno'

    def btn_at_sms_ligacao_naosoualuno(self):
        self.manager.current = 'tela_menu_atendimento_at_sms_ligacao_naosoualuno'

    def voltar(self):
        self.manager.current = 'tela_menu_atendimento'
        