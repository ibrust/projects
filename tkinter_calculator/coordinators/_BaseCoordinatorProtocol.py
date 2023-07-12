from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable


class CoordinatorResult(Enum):
    """ the coordinator's return type, passed to finish().
        implementors should inherit from CoordinatorResult and specify
        enum cases that make sense given their coordinators design
        i.e.
        MyCoordinatorResult(CoordinatorResult):
            SUCCESS = 1
            FAILURE = 2
        """
    pass


class BaseCoordinatorProtocol(ABC):

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)

        def new_finish(self, result: CoordinatorResult, _finish=cls.finish):
            _finish(self, result)
            self.onFinishCallback(result)

        cls.finish = new_finish

    # TODO: add support for an input & output event subject, child coordinators

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def finish(self, result: CoordinatorResult):
        pass

    @property
    def onFinishCallback(self):
        """this block can be set by calling code. It executes when the coordinator finishes"""
        return self._onFinishCallback

    @onFinishCallback.setter
    def onFinishCallback(self, callback: Callable[[CoordinatorResult], None]):
        if not isinstance(callback, Callable):
            raise TypeError("property must be of type Callable")

        self._onFinishCallback = callback