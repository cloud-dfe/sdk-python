from src import Averbacao, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    averbacao = Averbacao(config)

    file_xml_base64 = averbacao.file_open("./examples/teste.xml")

    payload = {
        "xml": file_xml_base64,
        "usuario": "login",
        "senha": "senha",
        "codigo": "codigo",
        "chave": ""
    }

    print(payload)

    resp = averbacao.atm(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)