from ..views import *
from .._types import *
from ._CalculatorControllerDelegate import CalculatorControllerDelegate

__all__ = ['CalculatorController']

class CalculatorController(CalculatorViewDelegate):

    delegate: CalculatorControllerDelegate

    def __init__(self):
        self.delegate = None

    def buttonTap(self, viewModel, symbol: ButtonSymbol):
        if symbol.isDigitOrDecimal():
            if viewModel.hasExceededMaxDigits:
                return
            self.delegate.digitOrDecimalEntered(symbol)
        elif symbol.isMathOperation():
            self.delegate.handleMathOperation(symbol)
        elif symbol == ButtonSymbol.EQUALS:
            self.delegate.equals()
        elif symbol == ButtonSymbol.OFF:
            self.delegate.turnOff()
        elif symbol == ButtonSymbol.CLEAR:
            self.delegate.clear()
        elif symbol == ButtonSymbol.PLUSMINUS:
            self.delegate.toggleSign()
