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
        "periodo": "2020-10",
        "data": "2020-10-15",
        "cnpj": "06338788000127"
    }

    resp = dfe.buscaNfe(payload)

    print(resp)

    if resp.get("sucesso"):
        for doc in resp.get("docs", []):
            chave = doc.get("chave")

        for evento in resp.get("eventos_proprios", []):
            chave = doc.get("chave")

except Exception as error:
    print("Ocorreu um erro", error)