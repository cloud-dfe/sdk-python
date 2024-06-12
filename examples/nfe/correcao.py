from sdk_cloud_dfe import Nfe, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfe = Nfe(config)

    payload = {
        "chave": "41240514867632000161650010000325901687509174",
        "justificativa": "teste de correcao"
    }

    resp = nfe.correcao(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)