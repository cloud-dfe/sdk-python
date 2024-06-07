from src.Base import Base, ConfigBase

class Gnre(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def consulta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/gnre/{key}", [])
    
    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/gnre", payload)
    
    def config_uf(self, payload: any) -> any:
        return self.client.send("POST", "/gnre/configuf", payload)