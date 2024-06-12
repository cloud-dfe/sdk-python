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
        "codigo_municipio_carregamento": "2408003",
        "nome_municipio_carregamento": "Mossoró",
        "codigo_municipio_descarregamento": "5200050",
        "nome_municipio_descarregamento": "Abadia de Goiás",
        "chave_nfe": "50000000000000000000000000000000000000000001"
    };

    resp = mdfe.nfe(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)