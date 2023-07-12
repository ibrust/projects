from tkinter import *
from tkinter import ttk
from ._BaseViewProtocol import BaseViewProtocol
from abc import ABC, abstractmethod
from .._types import ButtonSymbol, Colors


class OperationButtonsViewDelegate(ABC):
    @abstractmethod
    def buttonTap(self, symbol: ButtonSymbol):
        pass

class OperationButtonsView(BaseViewProtocol):

    delegate: OperationButtonsViewDelegate

    def __init__(self, superView: Frame):
        self.delegate = None
        self.superView = superView

    def constructViews(self):
        self.mainFrame: Frame = ttk.Frame(self.superView, padding="0")

        symbols = [ButtonSymbol.ADD, ButtonSymbol.SUB, ButtonSymbol.MUL, ButtonSymbol.DIV, ButtonSymbol.EQUALS]
        self.buttons: [Button] = []
        for i in range(0, 5):
            button: Button = ttk.Button(self.mainFrame, text=symbols[i].value, command=lambda i=i: self.buttonTap(symbols[i]))
            self.buttons.append(button)

    def layoutViews(self):
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        for i in range(0, 5):
            self.buttons[i].configure(width=5)
            self.buttons[i].grid(column=0, row=i, padx=0, pady=0, sticky=(N, E, S, W))

    def styleViews(self):
        frameStyle = ttk.Style(self.superView)
        frameStyle.theme_use("alt")
        frameStyle.configure("OperationButtonsViewMainFrame.TFrame", background="black", borderwidth=1, relief='raised')
        self.mainFrame.configure(style="OperationButtonsViewMainFrame.TFrame")

        buttonStyle = ttk.Style(self.superView)
        buttonStyle.configure("OperationButton.TButton", foreground="black", background=Colors.TERNARY.value, borderwidth=1, relief='raised')
        for button in self.buttons:
            button.configure(style="OperationButton.TButton")

    def buttonTap(self, symbol: ButtonSymbol):
        self.delegate.buttonTap(symbol)