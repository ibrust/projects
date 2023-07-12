from enum import Enum

__all__ = ['ButtonSymbol']


class ButtonSymbol(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "x"
    DIV = "÷"
    EQUALS = "="
    OFF = "OFF"
    PLUSMINUS = "+/-"
    CLEAR = "C"
    DECIMAL = "."
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    ZERO = "0"

    def isDigitOrDecimal(self) -> bool:
        if self == ButtonSymbol.DECIMAL:
            return True
        for i in range(0, 10):
            if str(i) == self.value:
                return True
        return False

    def isMathOperation(self) -> bool:
        return self == ButtonSymbol.ADD or self == ButtonSymbol.SUB \
                or self == ButtonSymbol.MUL or self == ButtonSymbol.DIV