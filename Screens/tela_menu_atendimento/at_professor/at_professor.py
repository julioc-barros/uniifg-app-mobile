from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import webbrowser

class Tela_Menu_At_Professor(MDScreen):

    def btn_at_agendamento_online(self):
        self.manager.current = 'tela_menu_atendimento_at_professor_online'

    def btn_at_agendamento_presencial(self):
        self.manager.current = 'tela_menu_atendimento_at_professor_presencial'

    def voltar(self):
        self.manager.current = 'tela_menu_atendimento'
        