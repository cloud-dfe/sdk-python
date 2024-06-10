import re
import base64

from .Cliente import AMBIENTE_HOMOLOGACAO, AMBIENTE_PRODUCAO, Client

class ConfigBase():

    def __init__(
            self, 
            ambiente: int, 
            token:str,
            timeout: int,
            port: int,
            path_config: str = None,
            debug: bool = False
            ) -> None:
        
        self.ambiente: int = ambiente   
        self.token: str = token
        self.options: dict = {
            "timeout": timeout,
            "port": port,
            "debug": debug
        }
        self.path_config = path_config

class Base():

    def __init__(self, params: ConfigBase) -> None:
        
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
            self.params.ambiente = AMBIENTE_HOMOLOGACAO

        if params.ambiente != AMBIENTE_HOMOLOGACAO and params.ambiente != AMBIENTE_PRODUCAO:
            raise ValueError("O Ambiente deve ser 1-PRODUÇÃO ou 2 HOMOLOGAÇÃO.")
        
        config = {
            "ambiente": self.params.ambiente,
            "token": self.params.token,
            "options": self.options,
            "path_config": self.params.path_config
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