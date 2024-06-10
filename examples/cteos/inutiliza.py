from sdk_cloud_dfe import Cteos, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443,
        #DEFINA O DIRETÓRIO O ARQUIVO config.json ESTÁ
        path_config="config.json" 
    )

    cteos = Cteos(config)

    payload = {
        "numero_inicial": "67",
        "numero_final": "67",
        "serie": "1",
        "justificativa": "teste de inutilização"
    }

    resp = cteos.inutiliza(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)