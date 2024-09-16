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
        self.options: dict = {
            "timeout": timeout,
            "port": port,
            "debug": debug
        }

class Base():

    def __init__(self, params: ConfigBase, direction: str = "api") -> None:
        
        self.params = params

        if self.params.options:
            self.options = {
                "timeout": self.params.options.get("timeout"),
                "port": self.params.options.get("port"),
                "debug": self.params.options.get("debug"),
            }

        else:
            self.options = {
                "timeout": 60,
                "port": 443,
                "debug": False,
            }

        if not self.params.ambiente:
            self.params.ambiente = 2

        if params.ambiente != 1 and params.ambiente != 2:
            raise ValueError("O Ambiente deve ser 1-PRODUÇÃO ou 2 HOMOLOGAÇÃO.")
        
        config = {
            "ambiente": self.params.ambiente,
            "token": self.params.token,
            "options": self.options
        }

        self.client = Client(config, direction)

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