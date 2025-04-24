from abc import ABC, abstractmethod


class DataFilterI(ABC):  # Interface
    @abstractmethod
    def filtrar(self, atividades: list[dict]) -> list[dict]:
        raise NotImplementedError('Required method')
