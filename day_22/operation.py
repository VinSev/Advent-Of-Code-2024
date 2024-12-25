class Operation:
    def __init__(self) -> None:
        self.operations = [
            lambda x: x * 64,
            lambda x: x // 32,
            lambda x: x * 2048
        ]

    def apply(self, secret_number: int) -> int:
        for operation in self.operations:
            value = operation(secret_number)
            secret_number = self.mix(secret_number, value)
            secret_number = self.prune(secret_number)
        return secret_number

    @staticmethod
    def mix(secret_number: int, value: int) -> int:
        return secret_number ^ value

    @staticmethod
    def prune(secret_number: int) -> int:
        return secret_number % 16777216
