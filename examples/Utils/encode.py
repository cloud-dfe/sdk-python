from sdk_cloud_dfe import Util

try:
    data = "texto a ser codificado"
    resp = Util.encode(data)
    print(resp)
except Exception as e:
    print(e)
