from .Base import Base, ConfigBase

class Dte(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def buscaCte(self, payload: any) -> any:
        return self.client.send("POST", "/dfe/cte", payload)
    
    def buscaNfe(self, payload: any) -> any:
        return self.client.send("POST", "/dfe/nfe", payload)
    
    def downloadNfe(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/dfe/nfe/{key}")
    
    def buscaNfse(self, payload: any) -> any:
        return self.client.send("POST", "/dfe/nfse", payload)
    
    def downloadNfse(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/dfe/nfse/{key}")
    
    def downloadCte(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/dfe/cte/{key}")
    
    def eventos(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/dfe/eventos/{key}")
    
    def backup(self, payload: any) -> any:
        return self.client.send("POST", "/dfe/backup", payload)
    
    