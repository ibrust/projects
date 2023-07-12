from abc import ABC, abstractmethod
from tkinter import *


class BaseViewProtocol(ABC):
    '''
    base class interface for use by views throughout application
    subclasses must implement constructViews(), layoutViews(), and decorateViews().
    during initialization these will automatically be called in order
    '''

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)

        def new_init(self, *args, init=cls.__init__, **kwargs):
            init(self, *args, **kwargs)
            self.constructViews()
            self.layoutViews()
            self.styleViews()

        cls.__init__ = new_init

    @abstractmethod
    def __init__(self, superView: Frame):
        pass

    @abstractmethod
    def constructViews(self):
        "subclasses must provide an implementation to initialize their widgets"
        pass

    @abstractmethod
    def layoutViews(self):
        "subclasses must provide an implementation to arrange their widgets using tkinter's geometry managers"
        pass

    @abstractmethod
    def styleViews(self):
        "subclasses must provide an implementation to decorate their views with colors, font styling, etc."
        pass
