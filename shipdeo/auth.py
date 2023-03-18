import requests

class ShipdeoAuth:
    BASE_URL = 'https://auth-api-production.shipdeo.com'
    def __init__(self, client_id, client_secret) -> None:
        self.__client_id = client_id
        self.__client_secret = client_secret

    def get_token(self):
        params = {
            'client_id': self.__client_id,
            'client_secret': self.__client_secret,
            'grant_type':'client_credentials'
        }
        response =  requests.post(self.BASE_URL + '/oauth2/connect/token', data=params)
        if response.status_code == 200:
            return response.json()['accessToken']
        elif response.status_code == 500:
            raise Exception("Error Server")
        elif response.status_code == 400:
            raise Exception("Error Body")
        elif response.status_code == 401:
            raise Exception("Invaoid Auth")
        