from sdk_cloud_dfe import Util  # Supondo que Util seja o nome do arquivo e da classe

try:
    resp = Util.readFile("caminho_do_arquivo.xml")
    print(resp)
except Exception as e:
    print(e)
