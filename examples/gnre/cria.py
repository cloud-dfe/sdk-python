import time
from sdk_cloud_dfe import Gnre, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    gnre = Gnre(config)

    payload = {
        "numero": "6",
        "uf_favoverida": "RO",
        "ie_emitente_uf_favorecida": None,
        "tipo": "0",
        "valor": 12.55,
        "data_pagamento": "2022-05-22",
        "identificador_guia": "12345",
        "receitas": [
            {
                "codigo": "100102",
                "detalhamento": None,
                "data_vencimento": "2022-05-22",
                "convenio": "Convênio ICMS 142/18",
                "numero_controle": "1",
                "numero_controle_fecp": None,
                "documento_origem": {
                    "numero": "000000001",
                    "tipo": "10"
                },
                "produto": None,
                "referencia": {
                    "periodo": "0",
                    "mes": "05",
                    "ano": "2022",
                    "parcela": None
                },
                "valores": [
                    {
                        "valor": 12.55,
                        "tipo": "11"
                    }
                ],
                "contribuinte_destinatario": {
                    "cnpj": None,
                    "cpf": None,
                    "ie": None,
                    "razao": None,
                    "ibge": None
                },
                "extras": [
                    {
                        "codigo": "52",
                        "conteudo": "32220526434850000191550100000000011015892724"
                    }
                ]
            }
        ]
    }


    resp = gnre.cria(payload)

    print(resp)

    if resp.get("sucesso"):
        chave = resp.get("chave")
        if resp.get("codigo") == 5023:

            time.sleep(5)
            tentativa = 1

            while tentativa <= 5:
                payload = {
                    "chave": chave
                }
                respC = gnre.consulta(payload)
                if respC.get("codigo") != 5023:
                    if respC.get("sucesso"):
                        print(respC)
                        break
                    else:
                        print(respC)
                        break
                
                time.sleep(5)
                tentativa += 1
        else:
            print(resp)
    
    elif resp.get("codigo") in [5001, 5002]:
        print(resp.get("erros"))
    
    elif resp.get("codigo") == 5008:
        chave = resp.get("chave")

        print(resp)
        payload = {
            "chave": chave
        }

        respC = gnre.consulta(payload)
        if respC.get("sucesso"):
            print(respC)
        
        else:
            print(respC)

    else:
        print(resp) 

except Exception as error:
    print("Ocorreu um erro", error)