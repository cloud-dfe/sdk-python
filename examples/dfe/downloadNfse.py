import base64

from sdk_cloud_dfe import Dfe, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443,
        #DEFINA O DIRETÓRIO O ARQUIVO config.json ESTÁ
        path_config="config.json" 
    )

    dfe = Dfe(config)

    payload = {
        "chave": "50000000000000000000000000000000000000000000",
    }

    resp = dfe.downloadNfse(payload)

    print(resp)

    if resp.get("sucesso"):
        xml_base64 = resp.get("doc", {}).get("xml", "")
        pdf_base64 = resp.get("doc", {}).get("pdf", "")

        xml = base64.b64decode(xml_base64)
        pdf = base64.b64decode(pdf_base64)

        with open("document.xml", "wb") as xml_file:
            xml_file.write(xml)

        with open("document.xml", "wb") as pdf_file:
            pdf_file.write(pdf)

except Exception as error:
    print("Ocorreu um erro", error)