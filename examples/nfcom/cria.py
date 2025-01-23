import time
from sdk_cloud_dfe import Nfcom, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfcom = Nfcom(config)

    payload = {
        "numero": "3",
        "serie": "1",
        "data_emissao": "2024-06-20T13:23:00-03:00",
        "finalidade_emissao": "0",
        "tipo_faturamento": "0",
        "indicador_prepago": "0",
        "indicador_cessao_meios_rede": "0",
        "destinatario": {
            "nome": "HELIO WOLFF",
            "cpf": "06844990960",
            "cnpj": "",
            "id_outros": "",
            "inscricao_estadual": None,
            "indicador_inscricao_estadual": "9",
            "endereco": {
                "logradouro": "LOJA",
                "complemento": None,
                "numero": "SN",
                "bairro": "BANANAL",
                "codigo_municipio": "4314035",
                "nome_municipio": "Pareci Novo",
                "uf": "RS",
                "codigo_pais": "1058",
                "nome_pais": "Brasil",
                "cep": "95783000",
                "telefone": None,
                "email": None
            }
            },
        "assinante": {
            "codigo": "123",
            "tipo": "3",
            "servico": "4",
            "numero_contrato": "12345678",
            "data_inicio": "2022-01-01",
            "data_fim": "2022-01-01",
            "numero_terminal": None,
            "uf": None
        },
        "itens": [],
        "cobranca": {
            "data_competencia": "2024-06-01",
            "data_vencimento": "2024-06-30",
            "codigo_barras": "19872982798277298279287298728278272872872"
        },
        "informacoes_adicionais_contribuinte": ""
    };

    lista_itens = [
        {
        "numero_item": "1",
        "codigo_produto": "123",
        "descricao": "LP 1MB",
        "codigo_classificacao": "0400401",
        "cfop": "5301",
        "unidade_medida": "1",
        "quantidade": "1",
        "valor_unitario": "10.00",
        "valor_desconto": "0",
        "valor_outras_despesas": "0",
        "valor_bruto": "10.00",
        "indicador_devolucao": "0",
        "informacoes_adicionais": "teste",
        "imposto": {
            "icms": {
                "situacao_tributaria": "00",
                "valor_base_calculo": "10.00",
                "aliquota": "18.00",
                "valor": "1.80"
            },
            "fcp": {
                "aliquota": None,
                "valor": None
            }
        }
        }
    ]

    payload["itens"] = lista_itens

    resp = nfcom.cria(payload)

    print(resp)

    if resp.get("sucesso"):
        chave = resp.get("chave")
        time.sleep(15)
        
        payload = {
            "chave": chave
        }

        resp = nfcom.consulta(payload)

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

        resp = nfcom.consulta(payload)
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