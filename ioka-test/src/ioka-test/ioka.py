import os
import requests
from exceptions import NoApiKeyError, InvalidTokenError

KEY = os.environ.get("API_KEY")


class IokaBase:
    """
    Ioka API base class
    """

    __DB_KEYS = [KEY]
    __URL = "https://stage-api.ioka.kz"

    HEADERS = {
        "Content-Type": "application/json",
    }

    def __new__(cls, *args, **kwargs):
        # print(args)
        return super().__new__(cls)

    def __init__(self, key=None, *args, **kwargs) -> None:
        self.validate_key(key)
        self.HEADERS["API-KEY"] = key
        print(self.HEADERS)

    @classmethod
    def validate_key(cls, key):
        if key not in cls.__DB_KEYS:
            raise InvalidTokenError()


class Order:
    """
    The class provides attributes and methods for working with orders
    """

    def __init__(self) -> None:
        pass

    # GET

    def list(*args, **kwargs):
        """Getting list of orders"""
        return None

    def retrieve(self, id: int, *args, **kwargs):
        """Getting order by id"""
        return None

    def get_events(self, index, *args, **kwargs):
        "Getting events for specific order"
        return None

    def get_refunds(self, index, *args, **kwargs):
        "Getting refunds for specific order"
        return None

    def get_refund_by_id(self, order_id: int, *args, **kwargs):
        "Getting specific refund for order"
        return None

    # POST

    def create(self, payload: dict, *args, **kwargs):
        """Create order"""
        url = f"{self.__URL}/order"
        # response = requests.post(url=url, data=payload)
        return None

    def create_capture(self, order_id: int, payload: dict, *args, **kwargs):
        """Create capture for specific order"""
        return None

    def cancel(self, order_id: int, reason: dict = None, *args, **kwargs):
        "Cancel specific order"
        return None

    def refund(self, order_id: int, payload: dict = None, *args, **kwargs):
        "Refund specific order"
        return None


class Payment:
    """
    The class provides attributes and methods for working with payments
    """

    def __init__(self) -> None:
        pass

    # GET

    def list(*args, **kwargs):
        """Getting list of orders"""
        return None

    def retrieve(*args, **kwargs):
        """Getting payment by id"""
        return None

    # POST

    def create(self, order_id: int, payload: dict, *args, **kwargs):
        """Create card"""
        return None

    def create_by_id(self, order_id: int, payload: dict, *args, **kwargs):
        """Create card"""
        return None


class Customer:
    """
    The class provides attributes and methods for working with customers
    """

    def __init__(self) -> None:
        pass

    # GET

    def list(self, *args, **kwargs):
        """Getting list of customers"""
        return None

    def retrieve(self, id: int, *args, **kwargs):
        """Getting customer by id"""
        return None

    def events(self, id: int, *args, **kwargs):
        """Getting events for specific customer"""
        return None

    # POST

    def create(self, order_id: int, payload: dict, *args, **kwargs):
        """Create customer"""
        return None

    # DELETE

    def destroy(self, order_id: int, id: int, *args, **kwargs):
        """Delete customer by id"""
        return None


class Card:
    """
    The class provides attributes and methods for working with customers
    """

    def __init__(self) -> None:
        pass

    # GET

    def list(self, order_id: int, payload: dict, *args, **kwargs):
        """Getting customer's list of cards"""
        return None

    def retrieve(self, id: int, *args, **kwargs):
        """Getting customer's specific card"""
        return None

    # POST

    def create(self, id: int, payload: dict, *args, **kwargs):
        """Create binding for customer"""
        return None

    # DELETE

    def destroy(self, id: int, *args, **kwargs):
        """Delete card by id"""
        return None


class Webhook:
    """
    The class provides attributes and methods for working with webhooks
    """

    def __init__(self) -> None:
        pass

    # GET

    def list(self, *args, **kwargs):
        """Getting webhooks"""
        return None

    def retrieve(self, id: int, *args, **kwargs):
        """Getting webhook by id"""
        return None

    # POST

    def create(self, payload: dict, *args, **kwargs):
        """Create webhook"""
        return None

    # PATCH

    def update(self, id: int, payload: dict, *args, **kwargs):
        """Update webhook by id"""
        return None

    # DELETE

    def destroy(self, id: int, *args, **kwargs):
        """Delete webhook by id"""
        return None


class Dashboard:
    """
    The class provides attributes and methods for working with dashboards
    """

    def __init__(self) -> None:
        pass

    # GET

    def search(self, *args, **kwargs):
        return None

    def export(self, *args, **kwargs):
        return None
