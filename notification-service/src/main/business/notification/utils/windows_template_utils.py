from os import path

from src.main.domain.constants import TemplateConsts, PathConsts


class WindowsTemplateUtils:
    @staticmethod
    def get_default_atividade_template() -> dict:
        return {
            TemplateConsts.APP_ICON: path.abspath(PathConsts.APP_ICON),
            TemplateConsts.TITLE: '🔔 Atividade UNOPAR',
            TemplateConsts.MESSAGE: None # Preencher valor de message
        }