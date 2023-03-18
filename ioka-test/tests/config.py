import os
from dotenv import load_dotenv


load_dotenv()


API_URL = os.environ.get("API_URL")
API_KEY = os.environ.get("API_KEY")
HEADERS = {
    "API-KEY": API_KEY,
    "Content-Type": "application/json",
}
