from tkinter import *
from tkinter import ttk
from ._BaseViewProtocol import BaseViewProtocol
from ._DecimalButtonsView import DecimalButtonsView, DecimalButtonsViewDelegate
from ._OperationButtonsView import OperationButtonsView, OperationButtonsViewDelegate
from .._types import ButtonSymbol
from ._CalculatorViewDelegate import CalculatorViewDelegate

__all__ = ['CalculatorView']

class CalculatorView(BaseViewProtocol, DecimalButtonsViewDelegate, OperationButtonsViewDelegate):

    class Model:
        displayText: str
        hasExceededMaxDigits: bool

        def __init__(self, displayText="0", hasExceededMaxDigits=False):
            self.displayText = displayText
            self.hasExceededMaxDigits = hasExceededMaxDigits

    @property
    def viewModel(self):
        return self._viewModel

    @viewModel.setter
    def viewModel(self, viewModel: Model):
        if not isinstance(viewModel, CalculatorView.Model):
            raise TypeError("viewModel must be of type CalculatorView.Model")
        self._viewModel = viewModel
        self.applyModel()

    delegate: CalculatorViewDelegate

    def __init__(self, superView: Frame):
        self.viewModel = CalculatorView.Model()
        self.delegate = None
        self.superView = superView

    def constructViews(self):
        self.mainFrame: Frame = ttk.Frame(self.superView)
        self.runningTotalLabel = ttk.Label(self.mainFrame, text=self.viewModel.displayText)

        self.numericalButtonsViewFrame: Frame = ttk.Frame(self.mainFrame)
        self.numericalButtonsView = DecimalButtonsView(self.numericalButtonsViewFrame)
        self.numericalButtonsView.delegate = self

        self.operationalButtonsViewFrame: Frame = ttk.Frame(self.mainFrame)
        self.operationalButtonsView = OperationButtonsView(self.operationalButtonsViewFrame)
        self.operationalButtonsView.delegate = self

    def layoutViews(self):
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)
        self.mainFrame.configure(padding=8)

        self.runningTotalLabel.grid(column=0, columnspan=2, row=0, sticky=(N, W, E))
        self.runningTotalLabel.configure(padding=5)

        self.numericalButtonsViewFrame.grid(column=0, row=2, sticky=(S, W))
        self.operationalButtonsViewFrame.grid(column=1, row=1, rowspan=2, sticky=(N, S, E))

    def styleViews(self):
        frameStyle = ttk.Style(self.superView)
        frameStyle.theme_use("alt")
        frameStyle.configure("CalculatorViewMainFrame.TFrame",
                             background="black",
                             borderwidth=5,
                             relief='raised')
        self.mainFrame.configure(style="CalculatorViewMainFrame.TFrame")

        runningTotalStyle = ttk.Style(self.mainFrame)
        runningTotalStyle.theme_use("alt")
        runningTotalStyle.configure("CalculatorViewRunningTotal.TLabel",
                                    foreground="white",
                                    background="black",
                                    borderwidth=1,
                                    relief='raised')
        self.runningTotalLabel.configure(style="CalculatorViewRunningTotal.TLabel")

        numericalButtonsViewFrameStyle = ttk.Style(self.mainFrame)
        numericalButtonsViewFrameStyle.theme_use("alt")
        numericalButtonsViewFrameStyle.configure("numericalButtonsViewFrame.TFrame",
                                                 background="black",
                                                 borderwidth=1,
                                                 relief='raised')
        self.numericalButtonsViewFrame.configure(style="numericalButtonsViewFrame.TFrame")
        self.operationalButtonsViewFrame.configure(style="numericalButtonsViewFrame.TFrame")

    def applyModel(self):
        if not hasattr(self, "runningTotalLabel"):
            return
        self.runningTotalLabel["text"] = self.viewModel.displayText

    def buttonTap(self, symbol: ButtonSymbol):
        self.delegate.buttonTap(self.viewModel, symbol)