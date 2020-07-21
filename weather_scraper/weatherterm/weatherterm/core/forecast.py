from datetime import date
from .forecast_type import ForecastType

class Forecast:
    def __init__(self, current_temp, humidity, wind, high_temp=None, low_temp=None, description='', forecast_date=None, forecast_type=ForecastType.TODAY):
        self._current_temp = current_temp
        self._high_temp = high_temp
        self._low_temp = low_temp
        self._humidity = humidity
        self._wind = wind
        self._description = description
        self._forecast_type = forecast_type

        if forecast_date is None:
            self.forecast_date = date.today()
        else:
            self._forecast_date = forecast_date

    @property                                           #like a getter, allows you to use the method forecast_date like an attribute
    def forecast_date(self):
        return self._forecast_date

    @forecast_date.setter                               #allows you to set the method like an attribute and preserve dependencies
    def forecast_date(self, forecast_date):
        self._forecast_date = forecast_date.strftime("%a %b %d")

    @property
    def current_temp(self):
        return self._current_temp

    @property
    def humidity(self):
        return self._humidity

    @property
    def wind(self):
        return self._wind

    @property
    def description(self):
        return self._description

    def __str__(self):
        temperature = None
        offset = ' ' * 4
        if self._forecast_type == ForecastType.TODAY:
            temperature = f'{offset}{self._current_temp}\xb0\n{offset}High {self._high_temp}'
        else:
            temperature = f'{offset}High {self._high_temp}'
        if (self._high_temp != "--"):
            temperature += '\xb0 / '
        temperature += f' Low {self._low_temp}'
        if (self._low_temp != "--"):
            temperature += '\xb0 '

        return (f'>> {self.forecast_date}\n{temperature}({self._description})\n{offset}Wind: {self._wind} / Humidity: {self._humidity}\n')
