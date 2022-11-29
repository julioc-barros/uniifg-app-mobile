import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.core.window import Window
Window.size = (380,700)

# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "Screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "Screens/tela_inicial/telainicial.kv"),
        os.path.join(os.getcwd(), "Screens/tela_login/telalogin.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_principal/tela_menu_principal.kv"),

        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/tela_menu_atendimento.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_caa/at_caa.kv"),

        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_cac/at_cac.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_cac/at_cac_unidade/at_cac_unidade.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_cac/at_cac_contato/at_cac_contato.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_cac/at_cac_ingresso/at_cac_ingresso.kv"),

        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_agendamento/at_agendamento.kv"),

        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_professor/at_professor.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_professor/online/online.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_professor/presencial/presencial.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "Screens.screenmanager",
        "TelaInicial": "Screens.tela_inicial.telainicial",
        "TelaLogin": "Screens.tela_login.telalogin",
        "Tela_Menu_Principal": "Screens.tela_menu_principal.tela_menu_principal",

        "Tela_Menu_Atendimento": "Screens.tela_menu_atendimento.tela_menu_atendimento",
        "Tela_Menu_At_CAA":"Screens.tela_menu_atendimento.at_caa.at_caa",

        "Tela_Menu_At_CAC":"Screens.tela_menu_atendimento.at_cac.at_cac",
        "Tela_Menu_At_CAC_Unidades":"Screens.tela_menu_atendimento.at_cac.at_cac_unidade.at_cac_unidade",
        "Tela_Menu_At_CAC_Contato":"Screens.tela_menu_atendimento.at_cac.at_cac_contato.at_cac_contato",
        "Tela_Menu_At_CAC_Ingresso":"Screens.tela_menu_atendimento.at_cac.at_cac_ingresso.at_cac_ingresso",

        "Tela_Menu_At_Agendamento":"Screens.tela_menu_atendimento.at_agendamento.at_agendamento",

        "Tela_Menu_At_Professor":"Screens.tela_menu_atendimento.at_professor.at_professor",
        "Tela_Menu_At_Professor_Online":"Screens.tela_menu_atendimento.at_professor.online.online",
        "Tela_Menu_At_Professor_Presencial":"Screens.tela_menu_atendimento.at_professor.presencial.presencial",

    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"


        return Factory.MainScreenManager()

# finally, run the app
if __name__ == "__main__":
    LiveApp().run()