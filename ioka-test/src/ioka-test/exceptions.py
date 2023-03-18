class NoApiKeyError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "Вы не ввели токен"
        super().__init__(*args)

    def __str__(self) -> str:
        return self.message


class InvalidTokenError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "Неверный токен"
        super().__init__(*args)

    def __str__(self) -> str:
        return self.message
