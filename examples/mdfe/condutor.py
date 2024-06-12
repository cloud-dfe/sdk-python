from sdk_cloud_dfe import Mdfe, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    mdfe = Mdfe(config)

    payload = {
        "chave": "50000000000000000000000000000000000000000000",
        "nome": "TESTE NOME",
        "cpf": "01234567890"
    };

    resp = mdfe.condutor(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)