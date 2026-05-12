from Config import settings
from Authorization import authorization_data
import requests

def get_access_token():
    response = requests.post(settings.TOKEN_URL,
                        headers=authorization_data.headers,
                             data=authorization_data.body
                        )
    response_json = response.json()
    access_token = response_json["access_token"]

    return access_token

token = get_access_token()