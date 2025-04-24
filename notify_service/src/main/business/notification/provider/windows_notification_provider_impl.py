
from plyer import notification

from src.main.business.service.atividade_service import AtividadeService
from src.main.business.notification.provider.notification_provider_i import (
    NotificationProviderI,
)
from src.main.business.notification.templates.mes_windows_template_builder_impl import (
    TemplateBuilderI
)
from src.main.business.notification.templates.mes_windows_template_builder_impl import (
    MesWindowsTemplateBuilderImpl,
)
from src.main.business.notification.templates.semana_windows_template_builder_impl import (
    SemanaWindowsTemplateBuilderImpl,
)


class WindowsNotificationProviderImpl(NotificationProviderI):
    def __init__(self):
        self._notifier = notification
        self._atividade_service = AtividadeService()
        self._template_semana: TemplateBuilderI = SemanaWindowsTemplateBuilderImpl()
        self._template_mes: TemplateBuilderI = MesWindowsTemplateBuilderImpl()

    def notify(self, events: list[dict]) -> None:
        atividades_semana: list[dict] = self._atividade_service.filtrar_semana(atividades=events)
        atividades_mes: list[dict] = self._atividade_service.filtrar_mes(atividades=events)

        self._notificar_semana(atividades=atividades_semana)
        self._notificar_mes(atividades_mes=atividades_mes)

    def _notificar_semana(self, atividades: list[dict]) -> None:
        for key, value in self._template_semana.build(atividades=atividades).items():
            self._notifier.notify(**value, timeout=1)

    def _notificar_mes(self, atividades_mes: int) -> None:
        template: dict = self._template_mes.build(atividades_mes)
        self._notifier.notify(**template, timeout=1)
