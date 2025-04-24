from abc import abstractmethod, ABC


class DataProcessorI(ABC): # interface
    @abstractmethod
    def process(self, atividades: list[str]) -> list[dict]:
        raise NotImplementedError('Required method')