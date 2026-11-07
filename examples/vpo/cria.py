from sdk_cloud_dfe import Vpo, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    vpo = Vpo(config)

    payload = {
        "numero": "1001",
        "identificacao": "VIAGEM-77",
        "emissor": "SEMPARAR",
        "data_inicio": "2026-11-10 08:00:00",
        "data_fim": "2026-11-12 18:00:00",
        "rota": {
            "id": "58222",
            "indice": "0",
            "distancia_km": "45.279",
            "tipo_combustivel": "DIESEL"
        },
        "veiculo": {
            "placa": "BCD2E34",
            "categoria": "7"
        },
        "transportador": {
            "cnpj": "22333444000181",
            "rntrc": "87654321",
            "nome": "TRANSPORTADOR EXEMPLO LTDA"
        },
        "cte": "1234"
    }

    resp = vpo.cria(payload)

    print(resp)

    if resp.get("sucesso"):
        if resp.get("codigo") == 5023:
            pass  # lote em processamento: consultar pela chave ou esperar o webhook
        else:
            pass  # VPO comprado
    else:
        pass  # rejeição

except Exception as error:
    print("Ocorreu um erro", error)
