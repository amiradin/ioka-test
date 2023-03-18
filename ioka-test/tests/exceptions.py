class InvalidDateTimeFormatError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "Невалидный формат времени"
        super().__init__(*args)

    def __str__(self) -> str:
        return self.message
