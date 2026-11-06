from .Base import Base, ConfigBase


class Ciot(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/ciot", payload)

    def consulta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/ciot/{key}")

    def busca(self, payload: any) -> any:
        return self.client.send("POST", "/ciot/busca", payload)

    def cancela(self, payload: any) -> any:
        return self.client.send("POST", "/ciot/cancela", payload)

    def encerra(self, payload: any) -> any:
        return self.client.send("POST", "/ciot/encerra", payload)

    def retifica(self, payload: any) -> any:
        return self.client.send("POST", "/ciot/retifica", payload)

    def pdf(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/ciot/pdf/{key}")

    def transportador(self, payload: any) -> any:
        return self.client.send("POST", "/ciot/transportador", payload)
