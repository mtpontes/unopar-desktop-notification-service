import os
from typing import ClassVar
from dotenv import load_dotenv
from dataclasses import dataclass

from src.main.infra.config.environment_consts import (EnvConsts, NotificationProviderEnum)


@dataclass(frozen=True)
class AppConfig:
    enabled_providers: ClassVar[list[NotificationProviderEnum]]

    @classmethod
    def load(cls):
        load_dotenv()
        cls.enabled_providers = cls._get_providers_enabled_list()
        return cls

    @staticmethod
    def _get_providers_enabled_list() -> list[NotificationProviderEnum]:
        enable_providers: str =  os.getenv(EnvConsts.ENABLED_PROVIDERS)
        if ',' in enable_providers:
            enable_providers: list[str] = [provider.strip() for provider in enable_providers.split(',')]
        else:
            enable_providers: list[str] = [enable_providers]

        return [NotificationProviderEnum(provider.strip()) for provider in enable_providers]
