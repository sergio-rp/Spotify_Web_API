import os
from dotenv import load_dotenv

load_dotenv()

# Spotify URLs
SPOTIFY_URL = "https://open.spotify.com"
BASE_URL = "https://api.spotify.com"
DEVELOPER_DASHBOARD_URL = "https://developer.spotify.com/dashboard"
TOKEN_URL = "https://accounts.spotify.com/api/token"

# Endpoints
GET_ALBUM_URL = "/v1/albums/"

# Credentials — se leen del .env, nunca hardcodeadas
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# IDs de prueba
ALBUM_ID = "5sY6UIQ32GqwMLAfSNEaXb"