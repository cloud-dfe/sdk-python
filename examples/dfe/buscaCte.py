from sdk_cloud_dfe import Dfe, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    dfe = Dfe(config)

    payload = {
        "periodo": "2020-10",
        "data": "2020-10-15",
        "cnpj": "06338788000127"
    }

    resp = dfe.buscaCte(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)