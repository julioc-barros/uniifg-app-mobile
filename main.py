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

        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_coordenacao/at_coordenacao.kv"),

        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_biblioteca/at_biblioteca.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_biblioteca/unidade/unidade.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_biblioteca/cadastro/cadastro.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_biblioteca/locacao/locacao.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_biblioteca/multa/multa.kv"),

        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_carreiras/at_carreiras.kv"),

        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_sms_ligacao/at_sms_ligacao.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_sms_ligacao/soualuno/soualuno.kv"),
        os.path.join(os.getcwd(), "Screens/tela_menu_atendimento/at_sms_ligacao/naosoualuno/naosoualuno.kv"),

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

        "Tela_Menu_At_Coordenacao":"Screens.tela_menu_atendimento.at_coordenacao.at_coordenacao",

        "Tela_Menu_At_Biblioteca":"Screens.tela_menu_atendimento.at_biblioteca.at_biblioteca",
        "Tela_Menu_At_Biblioteca_Unidade":"Screens.tela_menu_atendimento.at_biblioteca.unidade.unidade",
        "Tela_Menu_At_Biblioteca_Cadastro":"Screens.tela_menu_atendimento.at_biblioteca.cadastro.cadastro",
        "Tela_Menu_At_Biblioteca_Locacao":"Screens.tela_menu_atendimento.at_biblioteca.locacao.locacao",
        "Tela_Menu_At_Biblioteca_Multa":"Screens.tela_menu_atendimento.at_biblioteca.multa.multa",

        "Tela_Menu_At_Carreiras":"Screens.tela_menu_atendimento.at_carreiras.at_carreiras",

        "Tela_Menu_At_Sms_Ligacao":"Screens.tela_menu_atendimento.at_sms_ligacao.at_sms_ligacao",
        "Tela_Menu_At_Sms_Ligacao_Soualuno":"Screens.tela_menu_atendimento.at_sms_ligacao.soualuno.soualuno",
        "Tela_Menu_At_Sms_Ligacao_Naosoualuno":"Screens.tela_menu_atendimento.at_sms_ligacao.naosoualuno.naosoualuno",

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