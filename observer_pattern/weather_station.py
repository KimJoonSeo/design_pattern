from observer_pattern.observer import Observer, CurrentConditionsDisplay, ForecastDisplay
from observer_pattern.subject import WeatherData


def main():
    weather_data: WeatherData = WeatherData()

    o1: Observer = CurrentConditionsDisplay(weather_data)
    o2: Observer = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(69, 74, 29.2)

if __name__ == "__main__":
    main()