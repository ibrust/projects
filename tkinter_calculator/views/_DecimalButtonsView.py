from tkinter import *
from tkinter import ttk
from ._BaseViewProtocol import BaseViewProtocol
from abc import ABC, abstractmethod
import math
from .._types import ButtonSymbol, Colors


class DecimalButtonsViewDelegate(ABC):
    @abstractmethod
    def buttonTap(self, symbol: ButtonSymbol):
        pass

class DecimalButtonsView(BaseViewProtocol):

    delegate: DecimalButtonsViewDelegate

    def __init__(self, superView: Frame):
        self.delegate = None
        self.superView = superView

    def constructViews(self):
        self.mainFrame: Frame = ttk.Frame(self.superView, padding="0")

        upperSymbols = [ButtonSymbol.CLEAR, ButtonSymbol.PLUSMINUS, ButtonSymbol.OFF]
        self.topButtons: [Button] = []
        for i in range(0, len(upperSymbols)):
            button: Button = ttk.Button(self.mainFrame, text=upperSymbols[i].value,
                                        command=lambda i=i: self.buttonTap(upperSymbols[i]))
            self.topButtons.append(button)

        self.digitButtons: [Button] = []
        for i in range(1, 10):
            self.digitButtons.append(ttk.Button(self.mainFrame,
                                                text=ButtonSymbol(str(i)).value,
                                                command=lambda i=i: self.buttonTap(ButtonSymbol(str(i)))))

        self.digitButtons.append(ttk.Button(self.mainFrame,
                                            text=ButtonSymbol.ZERO.value,
                                            command=lambda: self.buttonTap(ButtonSymbol.ZERO)))
        self.decimalButton: Button = ttk.Button(self.mainFrame,
                                                text=ButtonSymbol.DECIMAL.value,
                                                command=lambda: self.buttonTap(ButtonSymbol.DECIMAL))

    def layoutViews(self):
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        for i in range(0, len(self.topButtons)):
            self.topButtons[i].configure(width=5)
            self.topButtons[i].grid(column=i, row=0, padx=0, pady=0, sticky=(N, E, S, W))
        for i in range(0, len(self.digitButtons)):
            self.digitButtons[i].configure(width=5)
            self.digitButtons[i].grid(column=i % 3, row=math.floor(i / 3)+1, padx=0, pady=0, sticky=(N, E, S, W))
        self.digitButtons[-1].grid(column=0, columnspan=2, row=4, padx=0, pady=0, sticky=(N, E, S, W))

        self.decimalButton.configure(width=5)
        self.decimalButton.grid(column=2, row=4, padx=0, pady=0, sticky=(N, E, S, W))

    def styleViews(self):
        frameStyle = ttk.Style(self.superView)
        frameStyle.theme_use("alt")
        frameStyle.configure("DecimalButtonsViewMainFrame.TFrame", background=Colors.PRIMARY.value, borderwidth=1, relief='raised')
        self.mainFrame.configure(style="DecimalButtonsViewMainFrame.TFrame")

        topButtonStyle = ttk.Style(self.superView)
        topButtonStyle.configure("UtilityButton.TButton", foreground="black", background=Colors.SECONDARY.value, borderwidth=1, relief='raised')
        for button in self.topButtons:
            button.configure(style="UtilityButton.TButton")

        buttonStyle = ttk.Style(self.superView)
        buttonStyle.configure("DigitButton.TButton", foreground="black", background=Colors.PRIMARY.value, borderwidth=1, relief='raised')
        for button in self.digitButtons:
            button.configure(style="DigitButton.TButton")
        self.decimalButton.configure(style="DigitButton.TButton")

    def buttonTap(self, symbol: ButtonSymbol):
        self.delegate.buttonTap(symbol)