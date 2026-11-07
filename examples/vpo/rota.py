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
        "enderecos": [
            {
                "codigo_municipio": "3543402",
                "nome_municipio": "Ribeirão Preto",
                "uf": "SP"
            },
            {
                "codigo_municipio": "3505906",
                "nome_municipio": "Batatais",
                "uf": "SP"
            }
        ],
        "categoria": "7",
        "data_inicio": "2026-11-10 08:00:00",
        "tipo_combustivel": "DIESEL"
    }

    resp = vpo.rota(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)
