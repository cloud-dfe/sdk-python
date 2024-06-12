from sdk_cloud_dfe import Gnre, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443 
    )

    gnre = Gnre(config)

    payload = {
        "uf_favoverida": "RR",
        "codigo_receita": None,
        "curier": None
    }

    resp = gnre.config_uf(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)