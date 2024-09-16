import json

from .RequestAPI import RequestApi

URI = {
    "api":{
        1:"https://api.integranotas.com.br/v1",
        2:"https://hom-api.integranotas.com.br/v1"
    }
}

class Client():

    def __init__(self, params: dict, direction: str = "api") -> None:
        
        self.params = params

        if not self.params:
            raise ValueError("Devem ser passados os parametros básicos.")
        
        if params.get("ambiente") != 1 and params.get("ambiente") != 2:
            raise ValueError("O AMBIENTE deve ser 1-PRODUCÃO OU 2-HOMOLOCAÇÃO.")
        
        if not params.get("token") or not isinstance(params.get("token"), str) or not params.get("token").strip():
            raise ValueError("O TOKEN é obrigatório.")
        
        self.ambiente: int = params.get("ambiente")
        self.token: str = params.get("token")
        self.options: dict = params.get("options")

        self.base_uri = URI.get(direction).get(self.ambiente)

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