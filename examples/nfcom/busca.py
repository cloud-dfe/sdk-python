from sdk_cloud_dfe import Nfcom, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfcom = Nfcom(config)

    payload = {
        "numero_inicial": 1210,
        "numero_final": 1210,
        "serie": 1,
        "data_inicial": "2019-12-01",
        "data_final": "2019-12-31",
        "cancel_inicial": "2019-12-01",
        "cancel_final": "2019-12-31",
        "status": "1"
    }

    resp = nfcom.busca(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)