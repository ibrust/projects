import sys
from argparse import ArgumentParser
from weatherterm.core import parser_loader
from weatherterm.core import ForecastType
from weatherterm.core import Unit
from weatherterm.core import SetUnitAction

def _validate_forecast_args(args):
    if (args.forecast_option is None):
        err_msg = 'One of these arguments must be used: -td/---today, -5d/--fivedays, -10d/--tendays, -w/--weekend'
        print(f'{argparser.prog}: error: {err_msg}', file=sys.stderr)
        sys.exit()

parsers = parser_loader.load('./weatherterm/parsers')

argparser = ArgumentParser(prog='weatherterm', description='Weather info from weather.com on your terminal')

required = argparser.add_argument_group('required arguments')
required.add_argument('-p', '--parser', choices=parsers.keys(), required=True, dest='parser',
                       help=('Specify which parser is going to be used to scrape weather information'))

unit_values = [name.title() for name, value in Unit.__members__.items()]
argparser.add_argument('-u', '--unit', choices=unit_values, required=False, dest='unit', action=SetUnitAction,
                       help=('Specify the unit that will be used to display the temperatures'))

required.add_argument('-lat', '--latitude', required=True, dest='latitude',
                       help=('The latitude to use for locating the weather forecast'))
required.add_argument('-long', '--longitude', required=True, dest='longitude',
                       help=('The longitude to use for locating the weather forecast'))
argparser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
argparser.add_argument('-td', '--today', dest='forecast_option', action='store_const', const=ForecastType.TODAY,
                       help='Show the weather forecast for the current day')
argparser.add_argument('-5d', '--fiveday', dest='forecast_option', action='store_const', const=ForecastType.FIVEDAYS,
                       help='Show the weather forecast for the next five days')
argparser.add_argument('-10d', '--tenday', dest='forecast_option', action='store_const', const=ForecastType.TENDAYS,
                       help='Show the weather forecast for the next ten days')
argparser.add_argument('-wk', '--weekend', dest='forecast_option', action='store_const', const=ForecastType.WEEKEND,
                       help='Show the weather forecast for the weekend')

args = argparser.parse_args()
_validate_forecast_args(args)

cls = parsers[args.parser]
parser = cls()
results = parser.run(args)

for result in results:
    print("__________________________________\n", result, sep='', end='', flush=True)
