from src.RequestAPI import RequestApi

def teste():
    config = {
        "base_uri": "https://hom-api.integranotas.com.br/v1",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        "options": {
            "timeout": 60,
            "port": 443,
            "debug": True
        }
    }

    # Criando uma instância da classe HttpRequests
    http_requests = RequestApi(config)

    # Testando o método request para uma solicitação GET
    try:
        response_data = http_requests.request("GET", "/nfe/status")
        print("Resposta:", response_data)
    except Exception as e:
        print("Ocorreu um erro:", e)

teste()