import re
from weatherterm.core import Forecast
from weatherterm.core import Request
from weatherterm.core import Unit
from weatherterm.core import UnitConverter
from weatherterm.core import ForecastType
from weatherterm.core import Mapper
from bs4 import BeautifulSoup

class WeatherComParser:
    def __init__(self):
        self._forecast = {
            ForecastType.TODAY: self._today_forecast,
            ForecastType.TENDAYS: self._ten_days_forecast,
            ForecastType.FIVEDAYS: self._five_days_forecast,
            ForecastType.WEEKEND: self._weekend_forecast,
        }
        self._base_url = 'http://weather.com/weather/{day}/l/{lat},{long}'
        self._request = Request(self._base_url)
        self._temp_regex = re.compile('([0-9]+)\D{,2}([0-9]+)')
        self._only_digits_regex = re.compile('[0-9]+')
        self._unit_converter = UnitConverter(Unit.FAHRENHEIT)

    def _parse_list_forecast(self, content, args):
        criteria = {
            'data-time': 'span',
            'day-detail': 'span',
            'description': 'td',
            'temp': 'td',
            'wind': 'td',
            'humidity': 'td',
        }
        bs = BeautifulSoup(content, 'html.parser')
        forecast_data = bs.find('table', class_='twc-table')
        container = forecast_data.tbody

        return self._parse(container, criteria)

    def _prepare_data(self, results, args, forecast_size):
        forecast_results = []
        self._unit_converter.dest_unit = args.unit
        length = 0
        for item in results:
            if (length >= forecast_size):
                break
            length += 1
            match = self._temp_regex.search(item['temp'])
            if (match is not None):
                high_temp, low_temp = match.groups()

            day_forecast = Forecast(self._unit_converter.convert(item['temp']), item['humidity'], item['wind'],
                        high_temp=self._unit_converter.convert(high_temp), low_temp=self._unit_converter.convert(low_temp),
                        description=item['description'].strip(), forecast_date=f'{item["day-detail"]}',
                        forecast_type=self._forecast_type)

            forecast_results.append(day_forecast)

        return forecast_results

    def _ten_days_forecast(self, args):
        content, driver = self._request.fetch_data(args.forecast_option.value, args.latitude, args.longitude)
        driver.close()
        results = self._parse_list_forecast(content, args)
        return self._prepare_data(results, args, 10)

    def _five_days_forecast(self, args):
        content, driver = self._request.fetch_data(args.forecast_option.value, args.latitude, args.longitude)
        driver.close()
        results = self._parse_list_forecast(content, args)
        return self._prepare_data(results, args, 5)

    def _weekend_forecast(self, args):
        criteria = {
            'weather-cell': 'header',
            'temp': 'p',
            'weather-phrase': 'h3',
            'wind-conditions': 'p',
            'humidity': 'p'
        }
        mapper = Mapper()
        mapper.remap_key('wind-conditions', 'wind')
        mapper.remap_key('weather-phrase', 'description')
        mapper.remap_key('weather-cell', 'day-detail')
        content, driver = self._request.fetch_data(args.forecast_option.value, args.latitude, args.longitude)
        driver.close()

        bs = BeautifulSoup(content, 'html.parser')

        forecast_data = bs.find('section', class_='ls-mod')

        container = forecast_data.div.div
        partial_results = self._parse(container, criteria)
        results = mapper.remap(partial_results)

        return self._prepare_data(results, args, 3)

    def run(self, args):
        self._forecast_type = args.forecast_option
        forecast_function = self._forecast[args.forecast_option]
        return forecast_function(args)

    def _get_data(self, container, search_items):
        scraped_data = {}
        for key, value in search_items.items():
            result = container.find(value, class_=key)
            data = None if result is None else result.get_text()
            if data is not None:
                scraped_data[key] = data
        return scraped_data

    def _parse(self, container, criteria):
        results = [self._get_data(item, criteria) for item in container.children]
        return [result for result in results if result]

    def _clear_str_number(self, str_number):
        result = self._only_digits_regex.match(str_number)
        return '--' if result is None else result.group()

    def _get_additional_info(self, content):
        data = tuple(item.td.span.get_text() for item in content.table.tbody.children)
        return data[:2]

    def _today_forecast(self, args):
        criteria = {
            'today_nowcard-temp': 'div',
            'today_nowcard-phrase': 'div',
            'today_nowcard-hilo': 'div',
        }
        content, driver = self._request.fetch_data(args.forecast_option.value, args.latitude, args.longitude)
        driver.close()

        bs = BeautifulSoup(content, 'html.parser')
        container = bs.find('section', class_='today_nowcard-container')
        weather_conditions = self._parse(container, criteria)

        if len(weather_conditions) < 1:
            raise Exception('Could not parse weather forecast for today.')

        weatherinfo = weather_conditions[0]
        temp_regex = re.compile(('H\s+(\d+|\-{,2}).+'
                                 'L\s+(\d+|\-{,2})'))
        temp_info = temp_regex.search(weatherinfo['today_nowcard-hilo'])
        high_temp, low_temp = temp_info.groups()
        side = container.find('div', class_='today_nowcard-sidecar')
        wind, humidity = self._get_additional_info(side)

        curr_temp = self._clear_str_number(weatherinfo['today_nowcard-temp'])
        self._unit_converter.dest_unit = args.unit

        td_forecast = Forecast(self._unit_converter.convert(curr_temp), humidity, wind, high_temp=self._unit_converter.convert(high_temp), low_temp=self._unit_converter.convert(low_temp), description=weatherinfo['today_nowcard-phrase'])

        return [td_forecast]
