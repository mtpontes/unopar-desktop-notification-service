from abc import ABC, abstractmethod


class DataCollectorI(ABC):  # Interface
    @abstractmethod
    def collect(self, atividades: list[str]) -> list[str]:
        raise NotImplementedError('Required method')