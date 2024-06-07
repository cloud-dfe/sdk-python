from src.Base import Base, ConfigBase

class Emitente(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def token(self) -> any:
        return self.client.send("GET", "/emitente/token", [])
    
    def atualiza(self, payload: any) -> any:
        return self.client.send("PUT", "/emitente", payload)
    
    def mostra(self) -> any:
        return self.client.send("GET", "/emitente", [])