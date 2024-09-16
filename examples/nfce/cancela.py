from sdk_cloud_dfe import Nfce, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfce = Nfce(config)

    payload = {
        "chave": "50000000000000000000000000000000000000000000",
        "justificativa": "teste de cancelamento"
    }

    resp = nfce.cancela(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)