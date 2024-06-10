import json

from .RequestAPI import RequestApi

AMBIENTE_PRODUCAO = "1"
AMBIENTE_HOMOLOGACAO = "2"

class Client():

    def __init__(self, params: dict) -> None:

        def json_file(path) -> dict | None:
                    try:
                        with open(path, "r", encoding="utf-8") as file:
                            dados: dict = json.load(file)
                            return dados
                        
                    except FileNotFoundError:
                        raise ValueError(f"Arquivo não encontrado.")
                    
                    except json.JSONDecodeError:
                        raise ValueError(f"Erro ao decodificar o arquivo.")
        
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

        self.path_config = (params.get("path_config")) or "./config.json"


        try:
            json_base_uri = json_file(self.path_config)
            
            if self.ambiente :
                self.base_uri = json_base_uri.get("api")[self.ambiente]

            else:
                 raise ValueError("ambiente não está definido no config.json. [1 / 2]")

        except: 
             raise ValueError("Arquivo json não configurado corretamente. Acesse https://github.com/cloud-dfe/sdk-nodejs para obter informações de como configura-lo")

        config = {
            "base_uri": self.base_uri,
            "token": self.token,
            "options": self.options
        }


        self.client = RequestApi(config)

    def send(self, method: str, route:str, payload:any = None) -> any:
         
         try:
              response_data = self.client.request(method, route, payload)
              return response_data
         
         except Exception as error:
              raise ValueError("Erro ao enviar solicitação HTTP: ", error)