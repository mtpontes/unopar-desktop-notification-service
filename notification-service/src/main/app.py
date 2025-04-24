from src.main.domain.constants import PathConsts
from src.main.infra.utils.file_handler_utils import FileHandlerUtils
from src.main.business.transform.data_transform_i import DataTransformI
from src.main.business.transform.atividade_data_transform_impl import AtividadeDataTransformImpl
from src.main.business.notification.provider.notification_provider_i import NotificationProviderI


class App:
    def __init__(self, notification_providers: list[NotificationProviderI]):
        self.notification_providers: list[NotificationProviderI] = notification_providers
        self.data_transform: DataTransformI = AtividadeDataTransformImpl()

    def run(self) -> None:
        events: list[dict] = FileHandlerUtils.read_json(PathConsts.ARQUIVO_JSON)
        events: list[dict] = self.data_transform.transform(atividades=events)

        for provider in self.notification_providers:
            provider.notify(events=events)