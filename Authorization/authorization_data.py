import base64
from Config import settings


credentials = f"{settings.CLIENT_ID}:{settings.CLIENT_SECRET}"

credentials_base64 = base64.b64encode(credentials.encode()).decode()

headers = {
        "Authorization": f"Basic {credentials_base64}",
    "Content-Type": "application/x-www-form-urlencoded"

}

body = {"grant_type": "client_credentials"}