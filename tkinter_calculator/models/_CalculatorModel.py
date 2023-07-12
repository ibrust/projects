from reactivex.subject.subject import Subject
from ..controllers import CalculatorControllerDelegate
from .._types import ButtonSymbol
from ..helpers import reactiveProperty

__all__ = ['CalculatorModel']


class CalculatorModel(CalculatorControllerDelegate):
    class Data:
        previousOperand: str = reactiveProperty("previousOperand", str)
        currentOperand: str = reactiveProperty("currentOperand", str)
        publisher: Subject

        def __init__(self):
            self.publisher = Subject()
            self.previousOperand = None
            self.currentOperand = "0"

    publisher: Subject
    data: Data
    didJustPressEquals: bool
    didJustPressMathOperationButton: bool
    nextOperation: ButtonSymbol

    def __init__(self):
        self.publisher = Subject()
        self.data = CalculatorModel.Data()
        self.didJustPressEquals = False
        self.didJustPressMathOperationButton = False
        self.nextOperation = None

        # publish self.data publicly whenever the observed self.data properties change
        self.data.publisher.subscribe(
            on_next=lambda v: self.publisher.on_next(self.data)
        )

    def handleMathOperation(self, nextOperation: ButtonSymbol):
        self.didJustPressMathOperationButton = True
        self.didJustPressEquals = False
        self.calculate()
        self.nextOperation = nextOperation

    def equals(self):
        self.didJustPressMathOperationButton = False
        self.didJustPressEquals = True
        self.calculate()

    def calculate(self):
        if self.data.previousOperand is not None and self.nextOperation is not None:
            self.performMathOperation()
            self.nextOperation = None
            self.data.previousOperand = None

    def performMathOperation(self):
        def extractFloat(op: str):
            if op == "." or op == "":
                if self.nextOperation == ButtonSymbol.DIV or self.nextOperation == ButtonSymbol.MUL:
                    op = "1"
                else:
                    op = "0"
            if op[-1] == ".":
                op = op[:-1]
            return float(op)

        op1 = extractFloat(self.data.currentOperand)
        op2 = extractFloat(self.data.previousOperand)
        result = ""

        if self.nextOperation == ButtonSymbol.ADD:
            result = str(op1 + op2)
        elif self.nextOperation == ButtonSymbol.SUB:
            result = str(op2 - op1)
        elif self.nextOperation == ButtonSymbol.MUL:
            result = str(op1 * op2)
        elif self.nextOperation == ButtonSymbol.DIV:
            result = str(op2 / op1)

        if len(result) >= 3 and result[-2:] == ".0":
            result = result[:-2]
        self.data.currentOperand = result

    def digitOrDecimalEntered(self, symbol: ButtonSymbol):
        if self.didJustPressMathOperationButton:
            self.data.previousOperand = self.data.currentOperand
            self.data.currentOperand = symbol.value
            self.didJustPressMathOperationButton = False
            return
        if self.data.currentOperand == "0" or self.didJustPressEquals:
            self.didJustPressEquals = False
            self.data.currentOperand = symbol.value
            return
        if symbol != ButtonSymbol.DECIMAL or not "." in self.data.currentOperand:
            self.data.currentOperand = self.data.currentOperand + symbol.value
            return

    def clear(self):
        self.data.currentOperand = "0"
        self.data.previousOperand = None
        self.data.hasPressedDecimal = False

    def toggleSign(self):
        if self.data.currentOperand != "0" and self.data.currentOperand[0] != "-":
            self.data.currentOperand = "-" + self.data.currentOperand
        elif self.data.currentOperand[0] == "-":
            self.data.currentOperand = self.data.currentOperand[1:]

    def turnOff(self):
        exit(0)
