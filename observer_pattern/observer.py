from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from observer_pattern.subject import WeatherData

class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        pass

class ForecastDisplay(Observer):
    __current_pressure: float = 29.9
    __last_pressure: float
    weather_data: 'WeatherData'

    def __init__(self, weather_data: 'WeatherData') -> None:
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self) -> None:
        self.__last_pressure = self.__current_pressure
        self.__current_pressure = self.weather_data.get_pressure()
        self.display()

    def display(self) -> None:
        print("《Forecast Display》")
        print("Forecast: ")
        if self.__current_pressure > self.__last_pressure:
            print("Improving weather on the way!")
        elif self.__current_pressure == self.__last_pressure:
            print("More of the same")
        elif self.__current_pressure < self.__last_pressure:
            print("Watch out for cooler, rainy weather")
        print()

class CurrentConditionsDisplay(Observer):
    temperature: float
    humidity: float
    weather_data: 'WeatherData'

    def __init__(self, weather_data: 'WeatherData') -> None:
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self) -> None:
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.display()

    def display(self) -> None:
        print("《Current Condition Display》")
        print("Current conditions: " + str(self.temperature) + "F degrees and " + str(self.humidity) + "% humidity")
        print()