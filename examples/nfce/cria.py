from sdk_cloud_dfe import Nfce, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfce = Nfce(config)

    payload = {
        "natureza_operacao": "VENDA DENTRO DO ESTADO",
        "serie": "1",
        "numero": "101008",
        "data_emissao": "2021-06-26T15:20:00-03:00",
        "tipo_operacao": "1",
        "presenca_comprador": "1",
        "itens": [],
        "frete": {
            "modalidade_frete": "9"
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
            "informacoes_adicionais_item": "Valor aproximado tributos R$: 9,43 (4,20%) Fonte: IBPT"
        }
    ]

    payload["itens"] = lista_itens

    resp = nfce.cria(payload)

    print(resp)

    if resp.get("sucesso"):
        if resp.get("codigo") == 2:
            # aguardar a chave e consultar/ou esperar o webhook notificar quando for processada pela sefaz
            print(resp)
        else:
            # autorizado
            print(resp)

    elif resp.get("codigo") == 5001 or resp.get("codigo") == 5002:
        # erro nos campos
        print(resp)
    elif resp.get("codigo") == 5008 or resp.get("codigo") >= 7000:
        chave = resp.get("chave")

        print(resp)
        payload = {
            "chave": chave
        }

        resp = nfce.consulta(payload)
        if resp.get("codigo") != 5023:
            if resp.get("sucesso"):
                # autorizado
                print(resp)
            else:
                # rejeição
                print(resp)
        else:
            # em processamento
            print(resp)
    else:
        # rejeição
        print(resp)
        
except Exception as error:
    print("Ocorreu um erro", error)