import json


class FileHandlerUtils:
    @staticmethod
    def escrever_json(atividades: list[object] | list[dict], caminho: str = 'atividades.json') -> None:
        with open(caminho, 'w', encoding="utf-8") as file:
            json.dump(atividades, file, indent=4, ensure_ascii=False)
