import os
import requests
from .ioka.exceptions import NoApiKeyError, InvalidTokenError

KEY = os.environ.get("API_KEY")


class Ioka:
    __db_keys = ["KEY"]
    __URL = "https://stage-api.ioka.kz"
    HEADERS = {
        "API-KEY": None,
        "Content-Type": "application/json",
    }

    def __init__(self, key=None, *args, **kwargs) -> None:
        self.validate_key(key)
        self.HEADERS["API-KEY"] = key
        print(self.HEADERS)

    def create_order(self, order_data={}) -> None:
        url = f"{self.__URL}/order"
        response = requests.post(url=url, data=order_data)

    @classmethod
    def validate_key(cls, key):
        if key not in cls.__db_keys:
            raise InvalidTokenError()
