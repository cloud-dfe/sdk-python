from .Base import Base, ConfigBase

class Cte(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def status(self) -> any:
        return self.client.send("GET", "/cte/status")
    
    def consulta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/cte/{key}");
    
    def pdf(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET",  f"/cte/pdf/{key}")
    
    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/cte", payload)
    
    def busca(self, payload: any) -> any:
        return self.client.send("POST", "/cte/busca", payload)
    
    def cancela(self, payload: any) -> any:
        return self.client.send("POST", "/cte/cancela", payload)
    
    def correcao(self, payload: any) -> any:
        return self.client.send("POST", "/cte/correcao", payload)
    
    def inutiliza(self, payload: any) -> any:
        return self.client.send("POST", "/cte/inutiliza", payload)
    
    def backup(self, payload: any) -> any:
        return self.client.send("POST", "/cte/backup", payload)
    
    def importa(self, payload: any) -> any:
        return self.client.send("POST", "/cte/importa", payload)
    
    def preview(self, payload: any) -> any:
        return self.client.send("POST", "/cte/preview", payload)
    
    def desacordo(self, payload: any) -> any:
        return self.client.send("POST", "/cte/desacordo", payload)
    
    