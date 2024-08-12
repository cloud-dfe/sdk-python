import time
from sdk_cloud_dfe import Nfse, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
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
        time.sleep(5)
        tentativa = 1
        while tentativa <= 5:
            payload = {
                "chave": chave
            }
            resp_c = nfse.consulta(payload)
            if resp_c.get("codigo") != 5023:
                if resp_c.get("sucesso"):
                    print(resp)
                    break
            else:
                print(resp)
                break
        time.sleep(5)
        tentativa += 1

    elif resp.get("codigo") in [5001, 5002]:
        print(resp.get("erros"))
    
    elif resp.get("codigo") == 5008 or resp.get("codigo") >= 7000:
        chave = resp.get("chave")

        print(resp)
        payload = {
            "chave": chave
        }

        resp_c = nfse.consulta(payload)
        if resp_c.get("sucesso"):
            if resp_c.get("codigo") == 5023:
                print(resp_c)
        
        else:
            print(resp_c)

    else:
        print(resp)
        
except Exception as error:
    print("Ocorreu um erro", error)