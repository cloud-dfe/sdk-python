from .Base import Base, ConfigBase

class Nfse(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/nfse", payload)
    
    def preview(self, payload: any) -> any:
        return self.client.send("POST", "/nfse/preview", payload)
    
    def pdf(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("POST", f"/nfse/{key}")
    
    def consulta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/nfse/{key}")
    
    def cancela(self, payload: any) -> any:
        return self.client.send("POST", "/nfse/cancela", payload)
    
    def substitui(self, payload: any) -> any:
        return self.client.send("POST", "/nfse/substitui", payload)
    
    def busca(self, payload: any) -> any:
        return self.client.send("POST", "/nfse/busca", payload)
    
    def backup(self, payload: any) -> any:
        return self.client.send("POST", "/nfse/backup", payload)
    
    def localiza(self, payload: any) -> any:
        return self.client.send("POST", "/nfse/consulta", payload)
    
    def info(self, payload: any) -> any:
        ibge = payload.get("ibge")
        return self.client.send("GET", f"/nfse/info/{ibge}")
    
    def conflito(self, payload: any) -> any:
        return self.client.send("POST", "/nfse/conflito", payload)
    
    def offline(self) -> any:
        return self.client.send("GET", "/nfse/offline")
    
    def resolve(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", F"/nfse/resolve{key}", payload)