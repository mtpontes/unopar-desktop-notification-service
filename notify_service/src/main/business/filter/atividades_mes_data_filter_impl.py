from datetime import datetime

from src.main.domain.constants import AtividadeConsts
from src.main.business.filter.data_filter_i import DataFilterI


class AtividadesMesDataFilterImpl(DataFilterI):
    def filtrar(self, atividades: list[dict]) -> list[dict]:
        atividades_filtradas = []
        for atividade in atividades:
            mes_atual = datetime.now().month
            mes_inic_atividade = atividade[AtividadeConsts.DATA_INIC].month
            mes_fim_atividade = atividade[AtividadeConsts.DATA_FIM].month

            if mes_inic_atividade is mes_atual or mes_fim_atividade is mes_atual:
                atividades_filtradas.append(atividade)

        return atividades_filtradas
