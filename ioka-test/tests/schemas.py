import re
from pydantic import BaseModel, Field, validator
from enums import Currency

from exceptions import InvalidDateTimeFormatError

# 2023-03-17T20:41:18.115369


class Order(BaseModel):
    created_at: str
    shop_id: str
    id: str
    status: str
    amount: int
    currency: Currency
    capture_method: str
    external_id: str | None
    description: str | None
    extra_info: str | None
    mcc: str | None
    acquirer: str | None
    customer_id: str | None
    card_id: str | None
    attempts: int
    due_date: str | None
    checkout_url: str

    @validator("created_at")
    def check_phoneNumber_format(cls, value):
        regExs = r"^(19[7-9]\d|20[0-1]\d|202[0-3])-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0,1])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9].\d{6}$"
        if not re.search(regExs[0], value):
            return InvalidDateTimeFormatError()
        return value
