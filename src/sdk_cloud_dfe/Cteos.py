from .Base import Base, ConfigBase

class Cteos(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def status(self) -> any:
        return self.client.send("GET", "/cteos/status")
    
    def consulta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/cteos/{key}");
    
    def pdf(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET",  f"/cteos/pdf/{key}")
    
    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/cteos", payload)
    
    def busca(self, payload: any) -> any:
        return self.client.send("POST", "/cteos/busca", payload)
    
    def cancela(self, payload: any) -> any:
        return self.client.send("POST", "/cteos/cancela", payload)
    
    def correcao(self, payload: any) -> any:
        return self.client.send("POST", "/cteos/correcao", payload)
    
    def inutiliza(self, payload: any) -> any:
        return self.client.send("POST", "/cteos/inutiliza", payload)
    
    def backup(self, payload: any) -> any:
        return self.client.send("POST", "/cteos/backup", payload)
    
    def importa(self, payload: any) -> any:
        return self.client.send("POST", "/cteos/importa", payload)
    
    def preview(self, payload: any) -> any:
        return self.client.send("POST", "/cteos/preview", payload)
    
    def desacordo(self, payload: any) -> any:
        return self.client.send("POST", "/cteos/desacordo", payload)
    
    