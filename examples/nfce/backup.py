from sdk_cloud_dfe import Nfce, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfce = Nfce(config)

    payload = {
        "ano": "2021",
        "mes": "2"
    }

    resp = nfce.backup(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)