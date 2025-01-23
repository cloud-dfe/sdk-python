import time
from sdk_cloud_dfe import Nfse, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfse = Nfse(config)

    payload = {
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
            "codigo_municipio": "4119905",
            "itens": {
                "codigo_tributacao_municipio": "10500",
                "discriminacao": "Exemplo Serviço",
                "valor_servicos": "1.00",
                "valor_pis": "1.00",
                "valor_cofins": "1.00",
                "valor_inss": "1.00",
                "valor_ir": "1.00",
                "valor_csll": "1.00",
                "valor_outras": "1.00",
                "valor_aliquota": "1.00",
                "valor_desconto_incondicionado": "1.00"
            }
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

    resp = nfse.cria(payload)

    print(resp)

    if resp.get("sucesso"):
        chave = resp.get("chave")
        time.sleep(15)
        
        payload = {
            "chave": chave
        }

        resp = nfse.consulta(payload)

        if resp.get("codigo") != 5023:
            if resp.get("sucesso"):
                # autorizado
                print(resp)
            else:
                # rejeição
                print(resp)
        else:
            # nota em processamento
            # recomendamos que seja utilizado o metodo de consulta manual ou o webhook
            print(resp)

    elif resp.get("codigo") in [5001, 5002]:
        print(resp.get("erros"))
    
    elif resp.get("codigo") == 5008:
        chave = resp.get("chave")

        print(resp)
        payload = {
            "chave": chave
        }

        resp = nfse.consulta(payload)
        if resp.get("codigo") != 5023:
            if resp.get("sucesso"):
                print(resp)
            else:
                print(resp)
        else:
            print(resp)

    else:
        print(resp)
        
except Exception as error:
    print("Ocorreu um erro", error)