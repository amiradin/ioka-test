import requests
import config
from response import Response
from schemas import Order

URL = f"{config.API_URL}/orders"

fields = [
    "created_at",
    "shop_id",
    "id",
    "status",
    "amount",
    "currency",
    "capture_method",
    "external_id",
    "description",
    "extra_info",
    "mcc",
    "acquirer",
    "customer_id",
    "card_id",
    "attempts",
    "due_date",
    "checkout_url",
]


def test_get_orders():
    # response = Response(requests.get(url=URL, headers=config.HEADERS))
    rsp = requests.get(url=URL, headers=config.HEADERS)
    print(type(rsp.json()[0]["created_at"]))
    # response.assert_status_code(status_code=200).validate(schema=Order)


test_get_orders()
