from src.Base import Base, ConfigBase

class Averbacao(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def __repr__(self) -> str:
        return super().__repr__()

    def atm(self, payload: any) -> any:
        return self.client.send("POST", "/averbacao/atm", payload)
    
    def elt(self, payload: any) -> any:
        return self.client.send("POST", "/averbacao/elt", payload)
    
    def porto_seguro(self, payload: any) -> any:
        return self.client.send("POST", "/averbacao/portoseguro", payload)