from src.Base import Base, ConfigBase

class Nfce(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/nfce", payload)
    
    def preview(self, payload: any) -> any:
        return self.client.send("POST", "/nfce/preview", payload)
    
    def status(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", "/nfce", payload)
    
    def consulta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/nfce/{key}", payload)
    
    def busca(self, payload: any) -> any:
        return self.client.send("POST", "/nfce/busca", payload)
    
    def cancela(self, payload: any) -> any:
        return self.client.send("POST", "/nfce/cancela", payload)
    
    def offline(self) -> any:
        return self.client.send("GET", "/nfce/offline", [])
    
    def inutiliza(self, payload: any) -> any:
        return self.client.send("POST", "/nfce/inutiliza", payload)
    
    def pdf(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/nfce/pdf/{key}", [])
    
    def substitui(self, payload: any) -> any:
        return self.client.send("POST", "/nfce/substitui", payload)
    
    def backup(self, payload: any) -> any:
        return self.client.send("POST", "/nfce/backup", payload)
    
    def importa(self, payload: any) -> any:
        return self.client.send("POST", "/nfce/importa", payload)