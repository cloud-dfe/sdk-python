from .Base import Base, ConfigBase

class Softhouse(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def cria_emitente(self, payload: any) -> any:
        return self.client.send("POST", "/soft/emitente", payload)
    
    def atualiza_emitente(self, payload: any) -> any:
        return self.client.send("PUT", "/soft/emitente", payload)
    
    def mostra_emitente(self, payload: any) -> any:

        if not payload or not payload.get("get"):
            raise ValueError("Deve ser passado um CNPJ ou um CPF para visualizar o emitente.")
        
        doc = payload.get("doc")
        return self.client.send("GET", f"/soft/emitente/{doc}")
    
    def lista_emitente(self, payload: any) -> any:

        status = payload.get("status") or ""
        rota = "/soft/emitente"

        if status == "deletados" or status == "inativos":
            rota = "/soft/emitente/deletados"
        
        return self.client.send("GET", rota)
    
    def deleta_emitente(self, payload: any) -> any:

        if not payload or not payload.get("get"):
            raise ValueError("Deve ser passado um CNPJ ou um CPF para visualizar o emitente.")
        
        doc = payload.get("doc")
        return self.client.send("DELETE", f"/soft/emitente/{doc}")