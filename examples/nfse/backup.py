from src.sdk_cloud_dfe import Nfse, ConfigBase, AMBIENTE_HOMOLOGACAO

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
        "ano": "2021",
        "mes": "2"
    }

    resp = nfse.backup(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)