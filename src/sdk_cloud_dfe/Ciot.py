import re
from urllib.parse import quote

from .Base import Base, ConfigBase


class Ciot(Base):

    def __init__(self, params: ConfigBase) -> None:
        super().__init__(params)

    def cria(self, payload: any) -> any:
        return self.client.send("POST", "/ciot", payload)

    def consulta(self, payload: any) -> any:
        identificacao = Ciot.check_identificacao(payload)
        return self.client.send("GET", f"/ciot/{identificacao}")

    def busca(self, payload: any) -> any:
        return self.client.send("POST", "/ciot/busca", payload)

    def cancela(self, payload: any) -> any:
        return self.client.send("POST", "/ciot/cancela", payload)

    def encerra(self, payload: any) -> any:
        return self.client.send("POST", "/ciot/encerra", payload)

    def retifica(self, payload: any) -> any:
        return self.client.send("POST", "/ciot/retifica", payload)

    def pdf(self, payload: any) -> any:
        identificacao = Ciot.check_identificacao(payload)
        return self.client.send("GET", f"/ciot/pdf/{identificacao}")

    def transportador(self, payload: any) -> any:
        return self.client.send("POST", "/ciot/transportador", payload)

    @staticmethod
    def check_identificacao(payload: any) -> str:
        # o CIOT é identificado pela identificação informada na criação, não por chave de acesso
        identificacao = str(payload.get("identificacao") or "").strip()
        if not re.fullmatch(r"[A-Za-z0-9._-]{1,40}", identificacao):
            raise ValueError("A identificação do CIOT deve ter de 1 a 40 caracteres: letras, números, ponto, hífen ou sublinhado")
        return quote(identificacao, safe="")
