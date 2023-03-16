import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://stage-api.ioka.kz/v2/"
API_KEY = os.environ.get("API_KEY")
HEADERS = {
    "Authorization": f"API-KEY {API_KEY}",
    "Content-Type": "application/json",
}
