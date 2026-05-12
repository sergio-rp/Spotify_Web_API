import requests
from Config import settings

class BaseAPI:
    def __init__(self, headers):
        self.base_url = settings.BASE_URL
        self.headers = headers

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint, headers=self.headers)