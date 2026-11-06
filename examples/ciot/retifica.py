from sdk_cloud_dfe import Ciot, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    ciot = Ciot(config)

    payload = {
        "chave": "41261122333444000181927090000010011360347860",
        "data_fim": "2026-11-13",
        "valor_frete": "4800.00",
        "pagamentos": [
            {
                "forma": "1",
                "tipo": "5",
                "cnpj": "22333444000181",
                "chave_pix": "22333444000181",
                "vencimento": "2026-11-13",
                "valor": "4800.00"
            }
        ]
    }

    resp = ciot.retifica(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)
