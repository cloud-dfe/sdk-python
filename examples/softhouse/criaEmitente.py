from sdk_cloud_dfe import Softhouse, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    softhouse = Softhouse(config)

    payload = {
        "nome": "EMPRESA TESTE",
        "razao": "EMPRESA TESTE",
        "cnpj": "47853098000193",
        "cpf": "12345678901",
        "cnae": "12369875",
        "crt": "1",  # Regime tributário
        "ie": "12369875",
        "im": "12369875",
        "suframa": "12369875",
        "csc": "...",  # token para emissão de NFCe
        "cscid": "000001",
        "tar": "C92920029-12",  # tar BPe
        "login_prefeitura": None,
        "senha_prefeitura": None,
        "client_id_prefeitura": None,
        "client_secret_prefeitura": None,
        "telefone": "46998895532",
        "email": "empresa@teste.com",
        "rua": "TESTE",
        "numero": "1",
        "complemento": "NENHUM",
        "bairro": "TESTE",
        "municipio": "CIDADE TESTE",  # IBGE
        "cmun": "5300108",  # IBGE
        "uf": "PR",  # IBGE
        "cep": "85000100",
        "logo": "useyn56j4mx35m5j6_JSHh734khjd...saasjda",  # BASE 64
        "plano": "Emitente",
        "documentos": {
            "nfe": True,
            "nfce": True,
            "nfse": True,
            "mdfe": True,
            "cte": True,
            "cteos": True,
            "bpe": True,
            "dfe_nfe": True,
            "dfe_cte": True,
            "sintegra": True,
            "gnre": True
        }
    }

    resp = softhouse.cria_emitente(payload)

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)