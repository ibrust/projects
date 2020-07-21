from enum import Enum, unique

@unique
class ForecastType(Enum):
    TODAY = 'today'
    FIVEDAYS = 'fiveday'
    TENDAYS = 'tenday'
    WEEKEND = 'weekend'
