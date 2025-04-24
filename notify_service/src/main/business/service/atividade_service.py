from src.main.business.filter.data_filter_i import DataFilterI
from src.main.business.filter.atividades_mes_data_filter_impl import AtividadesMesDataFilterImpl
from src.main.business.filter.atividades_semana_data_filter_impl import AtividadesSemanaDataFilterImpl


class AtividadeService:
    def __init__(self):
        self._filtroMes: DataFilterI = AtividadesMesDataFilterImpl()
        self._filtroSemana: DataFilterI = AtividadesSemanaDataFilterImpl()

    def filtrar_mes(self, atividades: list[dict]) -> list[dict]:
        return self._filtroMes.filtrar(atividades)

    def filtrar_semana(self, atividades: list[dict]) -> list[dict]:
        return self._filtroSemana.filtrar(atividades)
