from .Base import Base, ConfigBase

class Averbacao(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def atm(self, payload: any) -> any:
        return self.client.send("POST", "/averbacao/atm", payload)
    
    def atm_cancela(self, payload: any) -> any:
        return self.client.send("POST", "/averbacao/atm/cancela", payload)
    
    def porto_seguro(self, payload: any) -> any:
        return self.client.send("POST", "/averbacao/portoseguro", payload)
    
    def porto_seguro_cancela(self, payload: any) -> any:
        return self.client.send("POST", "/averbacao/portoseguro/cancela", payload)
    
    def elt(self, payload: any) -> any:
        return self.client.send("POST", "/averbacao/elt", payload)
    