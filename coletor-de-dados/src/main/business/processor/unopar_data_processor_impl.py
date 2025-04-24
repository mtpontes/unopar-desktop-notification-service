from src.main.infra.utils.date_utils import DateUtils
from src.main.domain.contants import Constants, AtividadeConst
from src.main.business.processor.data_processor_i import DataProcessorI


class UnoparDataProcessorImpl(DataProcessorI):
    def process(self, atividades: list[str]) -> list[dict]:
        atividades = self._estruturarComoLista(atividades=atividades)
        atividades = self._estruturarComoDict(atividades=atividades)
        atividades = self._filtrarAtividades(atividades=atividades)
        return atividades

    def _estruturarComoLista(self, atividades: list[str]) -> list[list[str]]:
        return list(map(lambda atividade: atividade.split('\n')[:4], atividades))  # ':4' Limita aos dados relevantes

    def _estruturarComoDict(self, atividades: list[str]) -> list[list[str]]:
        return list(
            map(lambda atividade: {
                    AtividadeConst.MATERIA: atividade[0],
                    AtividadeConst.ATIVIDADE: atividade[1],
                    AtividadeConst.SUBTITULO: atividade[2],
                    AtividadeConst.DATA_INIC: self._tratar_data_inic(atividade[3]),
                    AtividadeConst.DATAS_FIM: self._tratar_data_fim(atividade[3]),
                },
                atividades
                )
            )

    def _tratar_data_inic(self, data: str):
        return self._split_datas(data=data, hour=0, minute=0, second=0)[0]

    def _tratar_data_fim(self, data: str):
        return self._split_datas(data=data, hour=23, minute=59, second=59)[1]

    def _split_datas(self, data: str, hour: int = 0, minute: int = 0, second: int = 0) -> list[str]:
        datas = data.split(': ')[1].split(' - ')
        for i in range(len(datas)):
            datas[i] = DateUtils.to_iso_8601(datas[i], hour, minute, second)

        return datas

    def _filtrarAtividades(self, atividades: list[list[str]]) -> list[list[str]]:
        return list(
            filter(lambda materia: all(
                materiaIndesejada.lower() not in materia[AtividadeConst.ATIVIDADE].lower()
                for materiaIndesejada in Constants.ATIVIDADES_SEM_PRAZO
            ), atividades)
        )