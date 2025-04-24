from abc import ABC, abstractmethod

class DataTransformI(ABC):  # Interface
    @abstractmethod
    def transform(self, atividades: list[dict]) -> list[dict]:
        raise NotImplementedError('Required method')
