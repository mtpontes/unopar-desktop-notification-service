import os
from datetime import timedelta

from src.main.infra.utils.date_utils import DateUtils
from src.main.domain.constants import AtividadeConsts, PathConsts, TemplateConsts


class WindowsNotificationTemplateUtils:
    @staticmethod
    def format_atividade(atividade: dict) -> dict:
        template: dict = WindowsNotificationTemplateUtils._get_default_atividade_template()
        message: str = f'📌 {atividade[AtividadeConsts.SUBTITULO]} prazo limite expira em '

        tempo_a_vencer: timedelta = atividade[AtividadeConsts.TEMPO_RESTANTE]
        if tempo_a_vencer.days <= 0:
            horas: int = tempo_a_vencer.seconds // 3600
            minutos: int = (tempo_a_vencer.seconds % 3600) // 60
            message += f'{horas:02d}:{minutos:02d} horas! \n'
        else:
            dias: str = 'dias' if tempo_a_vencer.days > 1 else 'dia'
            message += f'{tempo_a_vencer.days} {dias}! \n'

        data_limite_formatada: str = DateUtils.to_date_br_str(atividade[AtividadeConsts.DATA_FIM])
        message += f'📅 Prazo limite: {data_limite_formatada}'
        template['message'] = message
        return template

    @staticmethod
    def format_atividades_total(quantidade_atividades: int) -> dict:
        template = WindowsNotificationTemplateUtils._get_default_atividade_template()
        template['message'] = f'📌 Total de atividades no mês: {quantidade_atividades}'
        return template

    @staticmethod
    def _get_default_atividade_template() -> dict:
        return {
            TemplateConsts.APP_ICON: os.path.abspath(PathConsts.APP_ICON),
            TemplateConsts.TITLE: '🔔 Atividade UNOPAR',
            TemplateConsts.MESSAGE: None # Preencher valor de message
        }
