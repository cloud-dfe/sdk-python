import time
from sdk_cloud_dfe import Cteos, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443 
    )

    cteos = Cteos(config)

    payload = {
        "cfop": "5353",
        "natureza_operacao": "PRESTACAO DE SERVICO",
        "numero": "64",
        "serie": "1",
        "data_emissao": "2020-11-24T03:00:00-03:00",
        "tipo_operacao": "0",
        "codigo_municipio_envio": "2408003",
        "nome_municipio_envio": "MOSSORO",
        "uf_envio": "RN",
        "tipo_servico": "6",
        "codigo_municipio_inicio": "2408003",
        "nome_municipio_inicio": "Mossoro",
        "uf_inicio": "RN",
        "codigo_municipio_fim": "2408003",
        "nome_municipio_fim": "Mossoro",
        "uf_fim": "RN",
        "valores": {
            "servico": "0.00",
            "valor_total": "0.00",
            "valor_receber": "0.00",
            "quantidade": "10.00"
        },
        "imposto": {
            "icms": {
                "situacao_tributaria": "99",
                "valor_base_calculo": "0.00",
                "aliquota": "12.00",
                "valor": "0.00",
                "aliquota_reducao_base_calculo": "50.00"
            },
            "federais": {
                "valor_pis": "0.00",
                "valor_cofins": "0.00",
                "valor_ir": "12.00",
                "valor_inss": "0.00",
                "valor_csll": "50.00"
            }
        },
        "modal_rodoviario": {
            "taf": "020335171251",
            "numero_registro_estadual": "0203351712510203351712515"
        },
        "tomador": {
            "indicador_inscricao_estadual": "9",
            "cpf": "01234567890",
            "inscricao_estadual": None,
            "nome": "EMPRESA MODELO",
            "razao_social": "EMPRESA MODELO",
            "telefone": "8499995555",
            "endereco": {
                "logradouro": "AVENIDA TESTE",
                "numero": "444",
                "bairro": "CENTRO",
                "codigo_municipio": "2408003",
                "nome_municipio": "Mossoro",
                "cep": "59603330",
                "uf": "RN",
                "codigo_pais": "1058",
                "nome_pais": "BRASIL",
                "email": "teste@teste.com.br"
            }
        },
        "componentes_valor": [
            {
                "nome": "teste2",
                "valor": "1999.00"
            }
        ],
        "observacao": ""
    }

    resp = cteos.cria(payload)

    print(resp)

    if resp.get("sucesso"):
        chave = resp.get("chave")
        time.sleep(5)
        tentativa = 1
        while tentativa <= 5:
            payload = {
                "chave": chave
            }
            resp_c = cteos.consulta(payload)
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

        resp_c = cteos.consulta(payload)
        if resp_c.get("sucesso"):
            if resp_c.get("codigo") == 5023:
                print(resp_c)
        
        else:
            print(resp_c)

    else:
        print(resp)
        
except Exception as error:
    print("Ocorreu um erro", error)