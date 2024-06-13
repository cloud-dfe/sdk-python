# SDK em Python para API Integra Notas

Este SDK visa simplificar a integração do seu sistema com a nossa API, oferecendo classes com funções pré-definidas para acessar as rotas da API. Isso elimina a necessidade de desenvolver uma aplicação para se comunicar diretamente com a nossa API, tornando o processo mais eficiente e direto.

*Nota: Utilizamos a biblioteca request para fazer as requisições de nossa API.*

## Forma de instalação de nosso SDK:

```
pip install sdk-cloud-dfe
```

## Forma de uso:

```py
from sdk_cloud_dfe import Nfe, ConfigBase, AMBIENTE_HOMOLOGACAO

try:
    config = ConfigBase(
        ambiente=AMBIENTE_HOMOLOGACAO,
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbXAiOiJ0b2tlbl9leGVtcGxvIiwidXNyIjoidGsiLCJ0cCI6InRrIn0.Tva_viCMCeG3nkRYmi_RcJ6BtSzui60kdzIsuq5X-sQ",
        timeout=60,
        port=443
    )

    nfe = Nfe(config)

    resp = nfe.status()

    print(resp)

except Exception as error:
    print("Ocorreu um erro", error)
```

### Sobre dados de envio e retornos

Para saber os detalhes referente ao dados de envio e os retornos consulte nossa documentação [IntegraNotas Documentação](https://integranotas.com.br/doc).

### Veja alguns exemplos de consumi de nossa API nos link abaixo:

[Pasta de Exemplos](https://github.com/cloud-dfe/sdk-python/tree/master/examples)

[Utilitários](https://github.com/cloud-dfe/sdk-python/tree/master/examples/utils)

[Averbação](https://github.com/cloud-dfe/sdk-python/tree/master/examples/averbacao)

[Certificado Digital](https://github.com/cloud-dfe/sdk-python/tree/master/examples/certificado)

[CT-e](https://github.com/cloud-dfe/sdk-python/tree/master/examples/cte)

[CT-e OS](https://github.com/cloud-dfe/sdk-python/tree/master/examples/cteos)

[DF-e](https://github.com/cloud-dfe/sdk-python/tree/master/examples/dfe)

[Emitente](https://github.com/cloud-dfe/sdk-python/tree/master/examples/emitente)

[GNR-e](https://github.com/cloud-dfe/sdk-python/tree/master/examples/gnre)

[MDF-e](https://github.com/cloud-dfe/sdk-python/tree/master/examples/mdfe)

[NFC-e](https://github.com/cloud-dfe/sdk-python/tree/master/examples/nfce)

[NF-e](https://github.com/cloud-dfe/sdk-python/tree/master/examples/nfe)

[NFS-e](https://github.com/cloud-dfe/sdk-python/tree/master/examples/nfse)

[Softhouse](https://github.com/cloud-dfe/sdk-python/tree/master/examples/softhouse)