from src.Base import Base, ConfigBase

class Nfe(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/nfe", payload)
    
    def preview(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/preview", payload)
    
    def status(self) -> any:
        return self.client.send("POST", "/nfe/status", [])
    
    def consulta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", F"/nfe/{key}", [])
    
    def busca(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/busca", payload)
    
    def cancela(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/cancela", payload)
    
    def correcao(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/correcao", payload)
    
    def inutiliza(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/inutiliza", payload)
    
    def pdf(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/nfe/pdf/{key}", [])
    
    def etiqueta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/nfe/pdf/etiqueta/{key}", [])
    
    def manifesta(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/manisfesta", payload)
    
    def backup(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/backup", payload)
    
    def download(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/nfe/download/{key}", [])
    
    def recebidas(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/recebidas", payload)
    
    def interessado(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/interessado", payload)
    
    def importa(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/importa", payload)
    
    def comprovante(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/comprovante", payload)
    
    def cadastro(self, payload: any) -> any:
        return self.client.send("POST", "/nfe/cadastro", payload)