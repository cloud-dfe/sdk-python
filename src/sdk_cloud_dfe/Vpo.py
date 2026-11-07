from .Base import Base, ConfigBase


class Vpo(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/vpo/ailog", payload)

    def consulta(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/vpo/ailog/{key}")

    def busca(self, payload: any) -> any:
        return self.client.send("POST", "/vpo/ailog/busca", payload)

    def cancela(self, payload: any) -> any:
        return self.client.send("POST", "/vpo/ailog/cancela", payload)

    def reemite(self, payload: any) -> any:
        return self.client.send("POST", "/vpo/ailog/reemite", payload)

    def rota(self, payload: any) -> any:
        return self.client.send("POST", "/vpo/ailog/rota", payload)

    def pdf(self, payload: any) -> any:
        key = Base.check_key(payload)
        return self.client.send("GET", f"/vpo/ailog/pdf/{key}")

    def veiculo(self, payload: any) -> any:
        return self.client.send("POST", "/vpo/ailog/veiculo", payload)
