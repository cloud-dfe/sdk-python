from sdk_cloud_dfe import Util

try:
    resp = Util.readFile("caminho_do_arquivo.xml")
    print(resp)
except Exception as e:
    print(e)
