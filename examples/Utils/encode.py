from sdk_cloud_dfe import Util  # Supondo que Util seja o nome do arquivo e da classe

try:
    data = "texto a ser codificado"
    resp = Util.encode(data)
    print(resp)
except Exception as e:
    print(e)
