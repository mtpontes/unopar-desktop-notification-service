from src.main.business.notification.utils.windows_template_utils import WindowsTemplateUtils
from src.main.business.notification.templates.template_builder_i import TemplateBuilderI


class MesWindowsTemplateBuilderImpl(TemplateBuilderI):
    def build(self, atividades: list[dict]) -> dict:
        quantidade_atividades = len(atividades)
        
        template = WindowsTemplateUtils.get_default_atividade_template()
        template['message'] = f'📌 Total de atividades no mês: {quantidade_atividades}'
        return template