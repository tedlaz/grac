"""Line classes"""
from .account import Account


class LineBase:
    """Base line class"""

    DEBIT, CREDIT = 1, 2

    def __init__(self, code: str, value: float):
        self.account = Account(code)
        self.value = round(float(value), 2)

    def new_reversed_line(self):
        return LineBase(self.account.code, -self.value)

    def debit_credit(self):
        return self.CREDIT if self.value < 0 else self.DEBIT

    @property
    def value_float(self) -> float:
        return round(float(self.value), 2)

    @property
    def value_str(self) -> str:
        return str(self.value)

    @property
    def debit(self) -> float:
        return 0 if self.value < 0 else self.value

    @property
    def credit(self) -> float:
        return -self.value if self.value < 0 else 0


class Line(LineBase):
    """Accounting Line class"""

    def __init__(self, code: str, value: float, parent=None) -> None:
        super().__init__(code, value)
        self.head = parent

    def new_reversed_line(self):
        return Line(self.account.code, -self.value)

    def __repr__(self):
        return f"Line(account='{self.account}, value={self.value})"
