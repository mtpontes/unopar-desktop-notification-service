from src.main.app import App
from src.main.infra.config.app_config import AppConfig


AppConfig.load()
App().run()