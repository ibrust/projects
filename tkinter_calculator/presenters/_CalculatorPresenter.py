from reactivex.subject.subject import Subject
from ..models import CalculatorModel
from ..views import CalculatorView

__all__ = ['CalculatorPresenter']

class CalculatorPresenter:

    publisher: Subject
    MAX_DIGITS: int = 19
    def __init__(self):
        self.publisher = Subject()
        self.modelData = None

    @property
    def modelData(self):
        return None

    @modelData.setter
    def modelData(self, modelData: CalculatorModel.Data):
        if modelData is None:
            return
        if not isinstance(modelData, CalculatorModel.Data):
            raise TypeError("model must be of type CalculatorModel.Data")

        self.publisher.on_next(self._createViewModel(modelData))

    def _createViewModel(self, modelData: CalculatorModel.Data) -> CalculatorView.Model:
        displayText = modelData.currentOperand
        hasExceededMaxDigits = False
        if len(displayText) >= CalculatorPresenter.MAX_DIGITS:
            # TODO: add logic for handling scientific notation that exceeds the max digit limit
            displayText = displayText[:CalculatorPresenter.MAX_DIGITS:] + "..."
            hasExceededMaxDigits = True

        return CalculatorView.Model(
            displayText=displayText,
            hasExceededMaxDigits=hasExceededMaxDigits
        )
