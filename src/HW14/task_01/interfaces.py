from abc import ABC, abstractmethod


class FelineInterface(ABC):

    @abstractmethod
    def scratch(self):
        raise NotImplemented


class CanineInterface(ABC):
    @abstractmethod
    def swim(self):
        raise NotImplemented
