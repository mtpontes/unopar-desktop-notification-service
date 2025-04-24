import os
from typing import ClassVar
from dataclasses import dataclass

from dotenv import load_dotenv

from src.main.domain.contants import EnvConstants as EnvConst


@dataclass
class ScrapingConfig:
    url: str
    username: str
    password: str

    @classmethod
    def load_from_envs(cls) -> 'ScrapingConfig':
        required_vars = {
            "url": EnvConst.URL_UNOPAR,
            "username": EnvConst.INST_USERNAME,
            "password": EnvConst.INST_PASSWORD
        }

        values = {attr: os.getenv(env) for attr, env in required_vars.items()}
        missing = [env for attr, env in required_vars.items() if values[attr] is None]

        if missing:
            raise EnvironmentError(f'Faltando variáveis de ambiente exigidas: {', '.join(missing)}')

        return cls(**values)

class AppConfig:
    scraping: ClassVar[ScrapingConfig]
    
    @classmethod
    def load(cls):
        load_dotenv()
        cls.scraping = ScrapingConfig.load_from_envs()