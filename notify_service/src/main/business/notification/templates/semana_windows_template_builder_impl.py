from datetime import timedelta

from src.main.domain.constants import AtividadeConsts
from src.main.infra.utils.date_utils import DateUtils
from src.main.business.notification.utils.windows_template_utils import WindowsTemplateUtils
from src.main.business.notification.templates.template_builder_i import TemplateBuilderI


class SemanaWindowsTemplateBuilderImpl(TemplateBuilderI):
    def build(self, atividades: list[dict]) -> dict:
        templates: list[dict] = self._criar_templates(atividades=atividades)
        
        template_map: dict = {}
        for index in range(len(templates)):
            template_map[index] = templates[index]
        
        return template_map

    
    def _criar_templates(self, atividades: list[dict]) -> list[dict]:
        templates: list[dict] = []
        for atividade in atividades:
            template: dict = WindowsTemplateUtils.get_default_atividade_template()
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
            templates.append(template)
            
        return templates
