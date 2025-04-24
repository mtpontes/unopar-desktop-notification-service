from datetime import datetime

from src.main.infra.utils.date_utils import DateUtils
from src.main.domain.constants import AtividadeConsts, Consts
from src.main.business.transform.data_transform_i import DataTransformI


class AtividadeDataTransformImpl(DataTransformI):
    def transform(self, atividades: list[dict]) -> list[dict]:
        atividades = self._converte_str_para_datetime(atividades=atividades)
        atividades = self._adicionar_dias_para_vencer(atividades=atividades)
        return self._remover_atividades_vencidas(atividades=atividades)

    def _converte_str_para_datetime(self, atividades: list[dict]) -> list[dict]:
        for atividade in atividades:
            atividade[AtividadeConsts.DATA_INIC] = DateUtils.to_datetime(atividade[AtividadeConsts.DATA_INIC])
            atividade[AtividadeConsts.DATA_FIM] = DateUtils.to_datetime(atividade[AtividadeConsts.DATA_FIM])
        return atividades

    def _adicionar_dias_para_vencer(self, atividades: list[dict]) -> list[dict]:
        for atividade in atividades:
            today = datetime.now()
            fim_ativ = atividade[AtividadeConsts.DATA_FIM]

            dias_para_vencimento_atividade = (fim_ativ - today)
            atividade[AtividadeConsts.TEMPO_RESTANTE] = dias_para_vencimento_atividade

        return atividades

    def _remover_atividades_vencidas(self, atividades: list[dict]) -> list[dict]:
        atividades_limpas = []
        for atividade in atividades:
            if atividade[AtividadeConsts.TEMPO_RESTANTE].days >= Consts.NUMERO_ZERO:
                atividades_limpas.append(atividade)

        return atividades_limpas


