import requests as r

class Services:

    def __init__(self, config: dict) -> None:
        
        self.base_uri:str = config.get("base_uri") or "";
        
        self.timeout:int = config.get("timeout") or 60;
        
        self.port:int = config.get("port") or 443;
        
        self.debug:bool = config.get("debug") or False;
    
        self.error:dict = {
            "code": 0, 
            "message": ""
        }

    def request(self, method: str, route: str, headers=dict, payload: any = None):
        try:
            resp = r.request(
                method=method,
                url=f"{self.base_uri}{route}",
                timeout= self.timeout,
                headers= headers,
                json=payload,
                allow_redirects=True
            )

            resp.raise_for_status()

            if self.debug:
                print(f"Método: {method} - URL: {self.base_uri}{route}")

            resp.raise_for_status()

            return resp.json()
        
        except r.exceptions.RequestException as error:

            if self.debug:
                print(f"Método: {method} - URL: {self.base_uri}{route} - Error {error}")

            if hasattr(error, 'response') and error.response is not None:
                return error.response.json()
            else:
                raise Exception(f"Falha de comunicação: {error}")