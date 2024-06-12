from sdk_cloud_dfe import Certificado, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443 
    )

    certificado = Certificado(config)

    file_xml_base64 = certificado.file_open("caminho_do_arquivo.pfx")

    payload = {
        "certificado": file_xml_base64,
        "senha": "senha",
    }

    resp = certificado.atualiza(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)