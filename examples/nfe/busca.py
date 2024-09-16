from sdk_cloud_dfe import Nfe, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )
    nfe = Nfe(config)

    payload = {
        "numero_inicial": 1214,
        "numero_final": 101002,
        "serie": 1,
        #"data_inicial": "2019-12-01",
        #"data_final": "2019-12-31",
        #"cancel_inicial": "2019-12-01" - Cancelamento
        #"cancel_final": "2019-12-31"
    }

    resp = nfe.busca(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)