from sdk_cloud_dfe import Vpo, ConfigBase

try:
    config = ConfigBase(
        ambiente=2, # 1 - produção / 2 - homologação
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    vpo = Vpo(config)

    payload = {
        "numero_inicial": "1",
        "numero_final": "1999",
        "data_inicial": "2026-11-01",
        "data_final": "2026-11-30",
        "situacao": "COMPRADO",
        "pagina": "1"
    }

    resp = vpo.busca(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)
