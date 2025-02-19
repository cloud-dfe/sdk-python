import json

from .Services import Services

URI = {
    "api":{
        1:"https://api.integranotas.com.br/v1",
        2:"https://hom-api.integranotas.com.br/v1"
    }
}

class Client():

    def __init__(self, params: dict) -> None:

        if not params:
            raise ValueError("Devem ser passados os parametros básicos.")
        
        if params.get("ambiente") != 1 and params.get("ambiente") != 2:
            raise ValueError("O AMBIENTE deve ser 1-PRODUCÃO OU 2-HOMOLOCAÇÃO.")
        
        if not params.get("token") or not isinstance(params.get("token"), str) or not params.get("token").strip():
            raise ValueError("O TOKEN é obrigatório.")
        
        self.ambiente: int = params.get("ambiente")
        self.token: str = params.get("token")

        self.port: int = params.get("port", None)
        self.timeout: int = params.get("timeout", None)
        self.debug: bool = params.get("debug", None)
        
        if not params.get("port") or not params.get("timeout"):
            self.port = params["options"].get("port")
            self.timeout = params["options"].get("timeout")
            self.debug = params["options"].get("debug")

        self.base_uri = URI.get("api").get(self.ambiente)

        config = {
            "base_uri": self.base_uri,
            "token": self.token,
            "port": self.port,
            "timeout": self.timeout,
            "debug": self.debug
        }

        self.client = Services(config)

    def send(self, method: str, route:str, payload:any = None) -> any:
         try:
            headers: dict = {
                "Authorization": self.token,
                "Content-Type": "application/json",
                "Accept": "application/json"
            }

            response_data = self.client.request(method, route, headers, payload)
            return response_data
         
         except Exception as error:
            raise ValueError("Erro ao enviar solicitação HTTP: ", error)
         
    def sendMultipart(self, route: str, payload: dict) -> any:
        try:
            headers: dict = {
                "Authorization": self.token,
                "Content-Type": "multipart/form-data",
                "Accept": "application/json"
            }

            response_data = self.client.request("POST", route, headers, payload)
            return response_data
        
        except Exception as error:
            raise ValueError("Erro ao enviar solicitação HTTP: ", error)