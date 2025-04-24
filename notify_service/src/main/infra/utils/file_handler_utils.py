import os
import json


class FileHandlerUtils:

    @staticmethod
    def read_json(path: str) -> list[dict]:
        atividades = None
        caminho_arquivo = os.path.abspath(path)
        with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
            atividades: list = json.load(file)

        return atividades