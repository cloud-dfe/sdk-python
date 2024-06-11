from sdk_cloud_dfe import Nfse, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443,
        #DEFINA O DIRETÓRIO O ARQUIVO config.json ESTÁ
        path_config="config.json" 
    )

    nfse = Nfse(config)

    payload = {
        "numero_rps_inicial": 15,
        "numero_rps_final": 15,
        "serie_rps": "0",
        # "numero_nfse_inicial": 1210,
        # "numero_nfse_final": 1210,
        # "data_inicial": "2019-12-01",  # Autorização
        # "data_final": "2019-12-31",
        # "cancel_inicial": "2019-12-01",  # Cancelamento
        # "cancel_final": "2019-12-31"
    }

    resp = nfse.busca(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)