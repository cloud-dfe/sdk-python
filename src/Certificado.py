from src.Base import Base, ConfigBase

class Certificado(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def atualiza(self, payload: any) -> any:
        return self.client.send("POST", "/certificado", payload)
    
    def mostra(self) -> any:
        return self.client.send("GET", "/certificado", "[]")