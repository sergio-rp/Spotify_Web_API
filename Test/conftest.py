import pytest
import base64
import requests
from Config import settings

@pytest.fixture(scope="session")
def auth_headers():
    credentials = f"{settings.CLIENT_ID}:{settings.CLIENT_SECRET}"
    encoded = base64.b64encode(credentials.encode()).decode()
    response = requests.post(settings.TOKEN_URL, headers={
        "Authorization": f"Basic {encoded}",
        "Content-Type": "application/x-www-form-urlencoded"
    }, data={"grant_type": "client_credentials"})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}