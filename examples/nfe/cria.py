import time
from sdk_cloud_dfe import Nfe, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfe = Nfe(config)

    payload = {
        "natureza_operacao": "VENDA DENTRO DO ESTADO",
        "serie": "1",
        "numero": "101007",
        "data_emissao": "2021-06-26T13:00:00-03:00",
        "data_entrada_saida": "2021-06-26T13:00:00-03:00",
        "tipo_operacao": "1",
        "finalidade_emissao": "1",
        "consumidor_final": "1",
        "presenca_comprador": "9",
        "intermediario": {
            "indicador": "0"
        },
        "notas_referenciadas": [
            {
                "nfe": {
                    "chave": "50000000000000000000000000000000000000000000"
                }
            }
        ],
        "destinatario": {
            "cpf": "01234567890",
            "nome": "EMPRESA MODELO",
            "indicador_inscricao_estadual": "9",
            "inscricao_estadual": None,
            "endereco": {
                "logradouro": "AVENIDA TESTE",
                "numero": "444",
                "bairro": "CENTRO",
                "codigo_municipio": "4108403",
                "nome_municipio": "Mossoro",
                "uf": "PR",
                "cep": "59653120",
                "codigo_pais": "1058",
                "nome_pais": "BRASIL",
                "telefone": "8499995555"
            }
        },
        "itens": [],
        "frete": {
            "modalidade_frete": "0",
            "volumes": [
                {
                    "quantidade": "10",
                    "especie": None,
                    "marca": "TESTE",
                    "numero": None,
                    "peso_liquido": 500,
                    "peso_bruto": 500
                }
            ]
        },
        "cobranca": {
            "fatura": {
                "numero": "1035.00",
                "valor_original": "224.50",
                "valor_desconto": "0.00",
                "valor_liquido": "224.50"
            }
        },
        "pagamento": {
            "formas_pagamento": [
                {
                    "meio_pagamento": "01",
                    "valor": "224.50"
                }
            ]
        },
        "informacoes_adicionais_contribuinte": "PV: 3325 * Rep: DIRETO * Motorista:  * Forma Pagto: 04 DIAS * teste de observação para a nota fiscal * Valor aproximado tributos R$9,43 (4,20%) Fonte: IBPT",
        "pessoas_autorizadas": [
            {
                "cnpj": "96256273000170"
            },
            {
                "cnpj": "80681257000195"
            }
        ]
    }

    # carrega os itens
    lista_itens = [
        {
            "numero_item": "1",
            "codigo_produto": "000297",
            "descricao": "SAL GROSSO 50KGS",
            "codigo_ncm": "84159020",
            "cfop": "5102",
            "unidade_comercial": "SC",
            "quantidade_comercial": 10,
            "valor_unitario_comercial": "22.45",
            "valor_bruto": "224.50",
            "unidade_tributavel": "SC",
            "quantidade_tributavel": "10.00",
            "valor_unitario_tributavel": "22.45",
            "origem": "0",
            "inclui_no_total": "1",
            "imposto": {
                "valor_aproximado_tributos": 9.43,
                "icms": {
                    "situacao_tributaria": "102",
                    "aliquota_credito_simples": "0",
                    "valor_credito_simples": "0",
                    "modalidade_base_calculo": "3",
                    "valor_base_calculo": "0.00",
                    "modalidade_base_calculo_st": "4",
                    "aliquota_reducao_base_calculo": "0.00",
                    "aliquota": "0.00",
                    "aliquota_final": "0.00",
                    "valor": "0.00",
                    "aliquota_margem_valor_adicionado_st": "0.00",
                    "aliquota_reducao_base_calculo_st": "0.00",
                    "valor_base_calculo_st": "0.00",
                    "aliquota_st": "0.00",
                    "valor_st": "0.00"
                },
                "fcp": {
                    "aliquota": "1.65"
                },
                "pis": {
                    "situacao_tributaria": "01",
                    "valor_base_calculo": 224.5,
                    "aliquota": "1.65",
                    "valor": "3.70"
                },
                "cofins": {
                    "situacao_tributaria": "01",
                    "valor_base_calculo": 224.5,
                    "aliquota": "7.60",
                    "valor": "17.06"
                }
            },
            "valor_desconto": 0,
            "valor_frete": 0,
            "valor_seguro": 0,
            "valor_outras_despesas": 0,
            "informacoes_adicionais": "Valor aproximado tributos R$: 9,43 (4,20%) Fonte: IBPT"
        }
    ]

    payload["itens"] = lista_itens

    resp = nfe.cria(payload)

    print(resp)

    if resp.get("sucesso"):
        chave = resp.get("chave")
        time.sleep(5)
        tentativa = 1
        while tentativa <= 5:
            payload = {
                "chave": chave
            }
            resp_c = nfe.consulta(payload)
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

        resp_c = nfe.consulta(payload)
        if resp_c.get("sucesso"):
            if resp_c.get("codigo") == 5023:
                print(resp_c)
        
        else:
            print(resp_c)

    else:
        print(resp)
        
except Exception as error:
    print("Ocorreu um erro", error)
