from sdk_cloud_dfe import AMBIENTE_PRODUCAO, Emitente, ConfigBase

try:
    config = ConfigBase(
        ambiente=AMBIENTE_PRODUCAO, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOjg3OTcsInVzciI6MzM5LCJ0cCI6MiwiaWF0IjoxNzI2NjcwMTQ4fQ.m0xe_qM74OXzKfp9tY5IGErqZsBJtI3EWIV5ARvKHOU",
        timeout=60,
        port=443
    )

    emitente = Emitente(config)

    resp = emitente.mostra()

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)