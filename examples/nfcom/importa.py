from sdk_cloud_dfe import Nfcom, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfcom = Nfcom(config)

    file_xml_base64 = nfcom.file_open("caminho_do_arquivo.xml")

    payload = {
        "xml": file_xml_base64
    }

    resp = nfcom.importa(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)