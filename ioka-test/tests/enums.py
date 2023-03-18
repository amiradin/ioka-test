from enum import Enum


class ErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"


class Currency(Enum):
    KZT = "KZT"
    USD = "USD"
    RUB = "RUB"


class CaptureMethod(Enum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"
