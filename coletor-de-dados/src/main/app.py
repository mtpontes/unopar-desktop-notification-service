from src.main.infra.utils.file_handler_utils import FileHandlerUtils
from src.main.business.colector.data_collector_i import DataCollectorI
from src.main.business.processor.data_processor_i import DataProcessorI
from src.main.business.colector.unopar_data_colector_impl import UnoparDataCollectorImpl
from src.main.business.processor.unopar_data_processor_impl import UnoparDataProcessorImpl


class App:
    def __init__(self) -> None:
        self._data_collector: DataCollectorI = UnoparDataCollectorImpl()
        self._data_process: DataProcessorI = UnoparDataProcessorImpl()

    def run(self) -> None:
        atividades: list[str] = self._data_collector.collect()
        atividades_dict: list[dict] = self._data_process.process(atividades=atividades)
        FileHandlerUtils.escrever_json(atividades=atividades_dict)
