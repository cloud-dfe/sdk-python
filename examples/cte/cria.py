import time
from sdk_cloud_dfe import Cte, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    cte = Cte(config)

    payload = {
        "cfop": "5932",
        "natureza_operacao": "PRESTACAO DE SERVIÇO",
        "numero": "66",
        "serie": "1",
        "data_emissao": "2021-06-22T03:00:00-03:00",
        "tipo_operacao": "0",
        "codigo_municipio_envio": "2408003",
        "nome_municipio_envio": "MOSSORO",
        "uf_envio": "RN",
        "tipo_servico": "0",
        "codigo_municipio_inicio": "2408003",
        "nome_municipio_inicio": "Mossoró",
        "uf_inicio": "RN",
        "codigo_municipio_fim": "2408003",
        "nome_municipio_fim": "Mossoró",
        "uf_fim": "RN",
        "retirar_mercadoria": "1",
        "detalhes_retirar": None,
        "tipo_programacao_entrega": "0",
        "sem_hora_tipo_hora_programada": "0",
        "remetente": {
            "cpf": "01234567890",
            "inscricao_estadual": None,
            "nome": "EMPRESA MODELO",
            "razao_social": "MODELO LTDA",
            "telefone": "8433163070",
            "endereco": {
                "logradouro": "AVENIDA TESTE",
                "numero": "444",
                "bairro": "CENTRO",
                "codigo_municipio": "2408003",
                "nome_municipio": "MOSSORÓ",
                "uf": "RN"
            }
        },
        "valores": {
            "valor_total": "0.00",
            "valor_receber": "0.00",
            "valor_total_carga": "224.50",
            "produto_predominante": "SAL",
            "quantidades": [
                {
                    "codigo_unidade_medida": "01",
                    "tipo_medida": "Peso Bruto",
                    "quantidade": "500.00"
                }
            ]
        },
        "imposto": {
            "icms": {
                "situacao_tributaria": "20",
                "valor_base_calculo": "0.00",
                "aliquota": "12.00",
                "valor": "0.00",
                "aliquota_reducao_base_calculo": "50.00"
            }
        },
        "nfes": [
            {
                "chave": "50000000000000000000000000000000000000000000"
            }
        ],
        "modal_rodoviario": {
            "rntrc": "02033517"
        },
        "destinatario": {
            "cpf": "01234567890",
            "inscricao_estadual": None,
            "nome": "EMPRESA MODELO",
            "telefone": "8499995555",
            "endereco": {
                "logradouro": "AVENIDA TESTE",
                "numero": "444",
                "bairro": "CENTRO",
                "codigo_municipio": "2408003",
                "nome_municipio": "Mossoró",
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
        "tomador": {
            "tipo": "3",
            "indicador_inscricao_estadual": "9"
        },
        "observacao": ""
    }

    resp = cte.cria(payload)

    print(resp)

    if resp.get("sucesso"):
        chave = resp.get("chave")
        time.sleep(15)
        
        payload = {
            "chave": chave
        }

        resp = cte.consulta(payload)

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

        resp = cte.consulta(payload)
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