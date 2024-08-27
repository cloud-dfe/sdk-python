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
        "tipo_operacao": "2",
        "tipo_transporte": None,
        "numero": "27",
        "serie": "1",
        "data_emissao": "2021-06-26T09:21:42-00:00",
        "uf_inicio": "RN",
        "uf_fim": "GO",
        "municipios_carregamento": [
            {
                "codigo_municipio": "2408003",
                "nome_municipio": "Mossoró"
            }
        ],
        "percursos": [
            {"uf": "PB"},
            {"uf": "PE"},
            {"uf": "BA"}
        ],
        "municipios_descarregamento": [
            {
                "codigo_municipio": "5200050",
                "nome_municipio": "Abadia de Goiás",
                "nfes": [
                    {
                        "chave": "50000000000000000000000000000000000000000000"
                    }
                ]
            }
        ],
        "valores": {
            "valor_total_carga": "100.00",
            "codigo_unidade_medida_peso_bruto": "01",
            "peso_bruto": "1000.000"
        },
        "informacao_adicional_fisco": None,
        "informacao_complementar": None,
        "modal_rodoviario": {
            "rntrc": "57838055",
            "ciot": [],
            "contratante": [],
            "vale_pedagio": [],
            "veiculo": {
                "codigo": "000000001",
                "placa": "FFF1257",
                "renavam": "335540391",
                "tara": "0",
                "tipo_rodado": "01",
                "tipo_carroceria": "00",
                "uf": "MT",
                "condutores": [
                    {
                        "nome": "JOAO TESTE",
                        "cpf": "01234567890"
                    }
                ]
            },
            "reboques": []
        }
    }

    resp = mdfe.preview(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)