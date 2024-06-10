import requests as r

class RequestApi ():

    def __init__(self, config: dict) -> None:
        self.base_uri:str = config.get("base_uri")
        self.token:str = config.get("token")

        self.headers = {
            "Authorization": config.get("token"),
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        self.options:dict = config.get("options")
        self.timeout:int = self.options.get("timeout") or 60
        self.port:int = self.options.get("port") or 443
        self.debug:bool = self.options.get("debug") or False

    def request(self, method: str, route: str, payload: any = None) -> dict:
        try:
            response = r.request(
                method=method,
                url=f"{self.base_uri}{route}",
                timeout= self.timeout,
                headers= self.headers,
                json=payload,
                allow_redirects=True
            )

            response.raise_for_status()

            if self.debug:
                print(f"Método: {method} - URL: {self.base_uri}{route}")

            response.raise_for_status()

            return response.json()
        
        except r.exceptions.RequestException as error:

            if self.debug:
                print(f"Método: {method} - URL: {self.base_uri}{route} - Error {error}")

            if hasattr(error, 'response') and error.response is not None:
                return error.response.json()
            else:
                raise RuntimeError(f"Falha de comunicação: {error}")