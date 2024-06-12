from sdk_cloud_dfe import Dfe, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    dfe = Dfe(config)

    payload = {
        "tipo": "nfe",
        "ano": "2020",
        "mes": "10"
    }

    resp = dfe.backup(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)