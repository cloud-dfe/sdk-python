from sdk_cloud_dfe import Ciot, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    ciot = Ciot(config)

    payload = {
        "numero": "1001",
        "identificacao": "PEDIDO-77",
        "tipo_operacao": "1",
        "data_inicio": "2026-11-10",
        "data_fim": "2026-11-12",
        "valor_frete": "4550.92",
        "contratante": {
            "cnpj": "11222333000181",
            "nome": "TRANSPORTADORA EXEMPLO LTDA",
            "rntrc": "12345678"
        },
        "contratado": {
            "cnpj": "22333444000181",
            "nome": "TRANSPORTADOR CONTRATADO LTDA",
            "rntrc": "87654321"
        },
        "destinatario": {
            "cnpj": "44555666000199",
            "nome": "DESTINATARIO EXEMPLO LTDA"
        },
        "motorista": {
            "cpf": "12345678909",
            "nome": "MOTORISTA EXEMPLO"
        },
        "veiculos": [
            {
                "placa": "BCD2E34",
                "eixos": "2",
                "rntrc": "87654321"
            }
        ],
        "carga": {
            "tipo": "05",
            "natureza": "8414",
            "peso": "1520"
        },
        "viagens": [
            {
                "quantidade": "1",
                "distancia": "560",
                "origem": {
                    "cep": "85000000",
                    "codigo_municipio": "4121604",
                    "municipio": "Renascença",
                    "uf": "PR"
                },
                "destino": {
                    "cep": "88300000",
                    "codigo_municipio": "4208203",
                    "municipio": "Itajaí",
                    "uf": "SC"
                }
            }
        ],
        "pagamentos": [
            {
                "forma": "1",
                "tipo": "5",
                "cnpj": "22333444000181",
                "chave_pix": "22333444000181",
                "vencimento": "2026-11-12",
                "valor": "4550.92"
            }
        ]
    }

    resp = ciot.cria(payload)

    print(resp)

    if resp.get("sucesso"):
        if resp.get("codigo") == 5023:
            pass  # lote em processamento: consultar pela chave ou esperar o webhook
        else:
            pass  # CIOT declarado
    else:
        pass  # rejeição

except Exception as error:
    print("Ocorreu um erro", error)
