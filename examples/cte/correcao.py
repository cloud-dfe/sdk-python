from sdk_cloud_dfe import Cte, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    cte = Cte(config)

    payload = {
        "chave": "50000000000000000000000000000000000000000000",
        "correcoes": [
            {
                "grupo_corrigido": "ide",
                "campo_corrigido": "natOp",
                "valor_corrigido": "PRESTACAO DE SERVIÇO"
            }
        ]
    }

    resp = cte.correcao(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)