from src.main.infra.config.environment_consts import NotificationProviderEnum
from src.main.business.notification.registry.notification_provider_registry import NotificationProviderRegistry
from src.main.business.notification.provider.windows_notification_provider_impl import WindowsNotificationProviderImpl


def create_notification_providers() -> NotificationProviderRegistry:
    """
    Cria e registra os provedores de notificação disponíveis na aplicação.
    """
    registry = NotificationProviderRegistry()
    registry \
        .register(NotificationProviderEnum.WINDOWS, WindowsNotificationProviderImpl()) \

    return registry
