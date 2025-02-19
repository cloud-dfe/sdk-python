import re
import base64

from .Cliente import Client

class ConfigBase():

    def __init__(
        self, 
        ambiente: int, 
        token:str,
        timeout: int,
        port: int,
        debug: bool = False
    ) -> None:
        
        self.ambiente: int = ambiente   
        self.token: str = token
        self.timeout: int = timeout
        self.port: int = port
        self.debug: bool = debug

class Base():

    def __init__(self, params: ConfigBase) -> None:

        if not params:
            raise ValueError("Devem ser passados os parametros básicos.")
        
        self.ambiente: int = params.ambiente
        self.token: str = params.token
        self.port: int = params.port
        self.timeout: int = params.timeout
        self.debug: bool = params.debug

        config: dict = {
            "ambiente": self.ambiente,
            "token": self.token,
            "port": self.port,
            "timeout": self.timeout,
            "debug": self.debug
        }

        self.client = Client(config)

    def check_key(payload: any) -> str:
        key = re.sub(r"[^0-9]", "", payload.get("chave"))
        if not key or len(key) != 44:
            raise ValueError("A chave deve conter 44 dígitos numéricos")
        return key
                    
    def file_open(self, path: str) -> str | None:
        try:
            with open(path, "rb") as file:
                conteudo = file.read()
                return base64.b64encode(conteudo).decode("utf-8")
            
        except FileNotFoundError as error:
             raise ValueError("Arquivo não encontrado: ", error)
        
        except Exception as error:
             raise ValueError("Erro ao tentar ler o arquivo: ", error)