from sdk_cloud_dfe import Cteos, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443 
    )

    cteos = Cteos(config)

    payload = {
        "chave": "50000000000000000000000000000000000000000000",
        "justificativa": "Não contratei esse serviço"
    }

    resp = cteos.desacordo(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)