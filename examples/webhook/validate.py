from sdk_cloud_dfe import Webhook

# * Este exemplo de verificação da assinatura dos dados enviados via webhook
# *
# * Este método indica se os dados passados pelo webhook são validodos
# *
# * NOTA: Será retornado uma Exception nos seguintes casos:
# * 1 - o payload não é um JSON válido
# * 2 - o payload não contêm a assinatura (campo signature)
# * 3 - o token está vazio (não foi passado um token)
# * 4 - Token ou assinatua incorreta (não foi possivel decriptar a assinatura)
# * 5 - a assinatura expirou (quando a assinatura tiver sido feita a mais de 5 minutos atras)

# token da softhouse do ambiente sendo usado (lembre-se existem dois token um para homologação e outro para produção e são diferentes)
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOjAsInVzciI6IjgiLCJ0cCI6MSwiaWF0IjoxNTg1NjkxNjA5fQ.s4GHUmafp_8Dkl3Hiiqe9KtHa5RLUg3X_2n6RIEXK34"

# payload do webhook em JSON (https://doc.cloud-dfe.com.br/webhook)
payload = '{"signature": "ojAm16Ye1cnnSxIM1D/8uUZROFYMitC6YleumaQx5W5IstqC1pdjvlact1q6LbE9f0OEjbtXZeVPYK/PtOfTmw=="}'

try:
    is_valid = Webhook.is_valid(token, payload)

    if is_valid:
        print("Assinatura válida")

except ValueError as e:

    print(f"Erro: {e}")
