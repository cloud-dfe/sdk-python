from sdk_cloud_dfe import Nfse, ConfigBase, AMBIENTE_HOMOLOGACAO

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
        "data_emissao_inicial": "2020-01-01",
        "data_emissao_final": "2020-01-31",
        "data_competencia_inicial": "2020-01-01",
        "data_competencia_final": "2020-01-31",
        "tomador_cnpj": None,
        "tomador_cpf": None,
        "tomador_im": None,
        "nfse_numero": None,
        "nfse_numero_inicial": None,
        "nfse_numero_final": None,
        "rps_numero": "15",
        "rps_serie": "0",
        "rps_tipo": "1",
        "pagina": "1"
    }

    resp = nfse.localiza(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)