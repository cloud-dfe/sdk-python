from src.Base import Base, ConfigBase

class Mdfe(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/mdfe", payload)
    
    def preview(self, payload: any) -> any:
        return self.client.send("POST", "/mdfe/preview", payload)
    
    def status(self) -> any:
        return self.client.send("GET", "/mdfe/status", [])
    
    def consulta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/mdfe/{key}", [])
    
    def busca(self, payload: any) -> any:
        return self.client.send("POST", "/mdfe/busca", payload)
    
    def cancela(self, payload: any) -> any:
        return self.client.send("POST", "/mdfe/cancela", payload)
    
    def encerra(self, payload: any) -> any:
        return self.client.send("POST", "/mdfe/encerra", payload)
    
    def condutor(self, payload: any) -> any:
        return self.client.send("POST", "/mdfe/condutor", payload)
    
    def offline(self) -> any:
        return self.client.send("GET", "/mdfe/offline", [])
    
    def pdf(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/mdfe/{key}", [])
    
    def backup(self, payload: any) -> any:
        return self.client.send("POST", "/mdfe/backup", payload)
    
    def nfe(self, payload: any) -> any:
        return self.client.send("POST", "/mdfe/nfe", payload)
    
    def abertos(self, payload: any) -> any:
        return self.client.send("POST", "/abertos", payload)
    
    def importa(self, payload: any) -> any:
        return self.client.send("POST", "/mdfe/importa", payload)