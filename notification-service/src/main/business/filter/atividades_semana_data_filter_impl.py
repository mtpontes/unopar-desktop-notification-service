from src.main.domain.constants import AtividadeConsts, Consts
from src.main.business.filter.data_filter_i import DataFilterI


class AtividadesSemanaDataFilterImpl(DataFilterI):
    def filtrar(self, atividades: list[dict]) -> list[dict]:
        atividades_filtradas = []

        for atividade in atividades:
            dias_para_vencer = atividade[AtividadeConsts.TEMPO_RESTANTE].days
            if dias_para_vencer >= Consts.NUMERO_ZERO and dias_para_vencer <= Consts.NUMERO_SETE:
                atividades_filtradas.append(atividade)

        return atividades_filtradas