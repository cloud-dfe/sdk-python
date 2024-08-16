from sdk_cloud_dfe import Webhook

if __name__ == "__main__":
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOjAsInVzciI6IjgiLCJ0cCI6MSwiaWF0IjoxNTg1NjkxNjA5fQ.s4GHUmafp_8Dkl3Hiiqe9KtHa5RLUg3X_2n6RIEXK34"
    payload = '{"signature": "ojAm16Ye1cnnSxIM1D/8uUZROFYMitC6YleumaQx5W5IstqC1pdjvlact1q6LbE9f0OEjbtXZeVPYK/PtOfTmw=="}'
    
    try:
        is_valid = Webhook.is_valid(token, payload)

        if is_valid:
            print("Assinatura válida")

    except ValueError as e:

        print(f"Erro: {e}")
