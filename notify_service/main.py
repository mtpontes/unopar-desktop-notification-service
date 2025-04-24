from src.main.app import App
from src.main.infra.config.app_config import AppConfig
from src.main.infra.config.environment_consts import NotificationProviderEnum
from src.main.infra.config.notification_provider_config import create_notification_providers
from src.main.business.notification.provider.notification_provider_i import NotificationProviderI
from src.main.business.notification.registry.notification_provider_registry import NotificationProviderRegistry


provider_keys: list[NotificationProviderEnum] = AppConfig.load().enabled_providers

registry: NotificationProviderRegistry = create_notification_providers()
notification_providers: list[NotificationProviderI] = registry.get_providers(provider_keys=provider_keys)

App(notification_providers=notification_providers).run()