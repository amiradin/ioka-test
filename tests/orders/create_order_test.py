import requests
import sys
from pprint import pprint


# URL = f"{API_URL}/orders"


def test_get_orders():
    response = requests.get(url=URL, headers=HEADERS)
    print(response.json())


# def test_create_order():
#     assert (1, 2, 3) == (1, 2, 3)
