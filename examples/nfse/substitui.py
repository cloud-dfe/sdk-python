from sdk_cloud_dfe import Nfse, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfse = Nfse(config)

    payload = payload = {
        "chave": "50000000000000000000000000000000000000000000",
        "codigo_cancelamento": "2",
        "motivo_cancelamento": "nota emitida com valor errado",
        "numero": "1",
        "serie": "0",
        "tipo": "1",
        "status": "1",
        "data_emissao": "2017-12-27T17:43:14-03:00",
        "tomador": {
            "cnpj": "12345678901234",
            "cpf": None,
            "im": None,
            "razao_social": "Fake Tecnologia Ltda",
            "endereco": {
                "logradouro": "Rua New Horizon",
                "numero": "16",
                "complemento": None,
                "bairro": "Jardim America",
                "codigo_municipio": "4119905",
                "uf": "PR",
                "cep": "81530945"
            }
        },
        "servico": {
            "codigo_tributacao_municipio": "10500",
            "discriminacao": "Exemplo Serviço",
            "codigo_municipio": "4119905",
            "valor_servicos": "1.00",
            "valor_pis": "1.00",
            "valor_cofins": "1.00",
            "valor_inss": "1.00",
            "valor_ir": "1.00",
            "valor_csll": "1.00",
            "valor_outras": "1.00",
            "valor_aliquota": "1.00",
            "valor_desconto_incondicionado": "1.00"
        },
        "intermediario": {
            "cnpj": "12345678901234",
            "cpf": None,
            "im": None,
            "razao_social": "Fake Tecnologia Ltda"
        },
        "obra": {
            "codigo": "2222",
            "art": "1111"
        }
    }

    resp = nfse.substitui(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)