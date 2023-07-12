from abc import ABC, abstractmethod
from .._types import ButtonSymbol

__all__ = ['CalculatorViewDelegate']

class CalculatorViewDelegate(ABC):
    @abstractmethod
    def buttonTap(self, viewModel, symbol: ButtonSymbol):
        pass