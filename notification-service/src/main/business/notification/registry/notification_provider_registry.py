from src.main.business.notification.provider.notification_provider_i import NotificationProviderI


class NotificationProviderRegistry:
    def __init__(self):
        self.providers: dict[str, NotificationProviderI] = {}

    def register(self, name: str, provider: NotificationProviderI):
        self.providers[name] = provider
        return self

    def get_providers(self, provider_keys: list[str]) -> list[NotificationProviderI]:
        return [self.providers[key] for key in provider_keys if key in self.providers]
