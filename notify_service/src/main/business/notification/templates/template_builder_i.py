from abc import abstractmethod, ABC


class TemplateBuilderI(ABC):
    @abstractmethod
    def build(self, atividades: dict) -> dict:
        raise NotImplementedError('Required method')
