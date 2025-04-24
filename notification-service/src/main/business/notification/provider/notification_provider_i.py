from abc import ABC, abstractmethod


class NotificationProviderI(ABC):  # Interface
    @abstractmethod
    def notify(self, events: list[dict]) -> None:
        raise NotImplementedError('Required method')
