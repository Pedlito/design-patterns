from abc import ABC, abstractmethod

class IBuilder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def setWindows(self) -> None:
        pass

    @abstractmethod
    def setDoors(self) -> None:
        pass

    @abstractmethod
    def setWalls(self) -> None:
        pass

    @abstractmethod
    def setRoof(self) -> None:
        pass

    @abstractmethod
    def setPool(self) -> None:
        pass