from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from observer_pattern.observer import Observer


class Subject(ABC):
    @abstractmethod
    def register_observer(self, o: 'Observer') -> None:
        pass

    @abstractmethod
    def remove_observer(self, o: 'Observer') -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class WeatherData(Subject):
    __observers: List['Observer']
    __temperature: float
    __humidity: float
    __pressure: float

    def __init__(self) -> None:
        self.__observers = []

    def register_observer(self, o: 'Observer'):
        self.__observers.append(o)

    def remove_observer(self, o: 'Observer'):
        self.__observers.remove(o)

    def notify_observers(self):
        for o in self.__observers:
            o.update()

    def get_temperature(self) -> float:
        return self.__temperature

    def get_humidity(self) -> float:
        return self.__humidity

    def get_pressure(self) -> float:
        return self.__pressure

    def measure_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure

        self.notify_observers()
