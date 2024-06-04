import json

from RequestAPI import RequestApi


AMBIENTE_PRODUCAO = 1
AMBIENTE_HOMOLOGACAO = 2

class Client():

    def __init__(self, params: dict) -> None:

        def jsonFile(path) -> dict | None:
                    try:
                        with open(path, "r", encoding="utf-8") as file:
                            dados: dict = json.load(file)
                            return dados
                        
                    except FileNotFoundError:
                        print(f"Arquivo não encontrado.")
                        return None
                    
                    except json.JSONDecodeError:
                        print(f"Erro ao decodificar o arquivo.")
                        return None
        
        self.params = params

        if not self.params:
            raise ValueError("Devem ser passados os parametros básicos.")
        
        if params.get("ambiente") != AMBIENTE_HOMOLOGACAO and params.get("ambiente") != AMBIENTE_PRODUCAO:
            raise ValueError("O AMBIENTE deve ser 1-PRODUCÃO OU 2-HOMOLOCAÇÃO.")
        
        if not params.get("token") or not isinstance(params.get("token"), str) or not params.get("token").strip():
            raise ValueError("O TOKEN é obrigatório.")
        
        self.ambiente: int = params.get("ambiente")
        self.token: str = params.get("token")
        self.options: dict = params.get("options")

        self.path_config = (params.get("path_config")) or "./src/config.json"

        try:
             
             path_config = jsonFile()