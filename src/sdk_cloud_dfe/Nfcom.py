from .Base import Base, ConfigBase

class Nfcom(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def status(self) -> any:
        return self.client.send("GET", "/nfcom/status")

    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/nfcom", payload)
    
    def consulta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/nfcom/{key}")
    
    def cancela(self, payload: any) -> any:
        return self.client.send("POST", "/nfcom/cancela", payload)
    
    def busca(self, payload: any) -> any:
        return self.client.send("POST", "/nfcom/busca", payload)
    
    def pdf(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/nfcom/pdf/{key}")
    
    def preview(self, payload: any) -> any:
        return self.client.send("POST", "/nfcom/preview", payload)
    
    def backup(self, payload: any) -> any:
        return self.client.send("POST", "/nfcom/backup", payload)
    
    def importa(self, payload: any) -> any:
        return self.client.send("POST", "/nfcom/importa", payload)