# Enter your code here. Read input from STDIN. Print output to STDOUT
kilos_to_pounds = lambda p: 2.20462  * p
pounds_to_kilos = lambda k: 0.453592 * k
pounds_to_grams = lambda p: p / 1000
kilos_to_grams = lambda k: k * 1000
meters_to_feet = lambda m: 3.28084 * m
feet_to_meters = lambda f: 0.3048 * f
farenheit_to_celsius = lambda f: (f - 32.0) * (5.0/9.0)
celsius_to_farenheit = lambda c: (c * 9.0/5.0) + 32.0

import sys
import re

thismodule = sys.modules[__name__]
whitelist = {
    'pounds': 'kilos',
    'kilos': 'pounds',
    'meters': 'feet',
    'feet': 'meters',
    'farenheit': 'celsius',
    'celsius': 'farenheit',
    'volts': 'gigavolts'
}
def is_allowed(source, dest):
    allowed = {
        source: whitelist.get(source, None)
        for k,v in whitelist.items()
        if source in whitelist and whitelist[source] == v
    }

    if not allowed:
        raise Exception(f'Cannot convert {source} to {dest}.')
    return True

def add(func, source, dest):
    if is_allowed(source, dest):
        setattr(thismodule, '{}_to_{}'.format(source, dest), func)
        return True
    return False

def convert(source, dest, value):
    if is_allowed(source, dest):
        val = getattr(thismodule, f'{source}_to_{dest}')(value)
        return val
    return None

print(convert('pounds', 'kilos', 10.0) == 4.53592)
print(convert('kilos', 'pounds', 10.0) == 22.0462)
print(convert('kilos', 'grams', 10.0) == 10000)
print(convert('pounds', 'grams', 10.0) == 4535.92)
print(convert('meters', 'feet', 10.0) == 32.8084)
print(convert('feet', 'meters', 10.0) == 3.048)
print(round(convert('farenheit', 'celsius', 10.0), 2) == -12.22)
print(convert('celsius', 'farenheit', 10.0) == 50.0)

volts_to_gigavolts = lambda v: v * 0.000000001
add(volts_to_gigavolts, 'volts', 'gigavolts')
print(convert('volts', 'gigavolts', 100))


maxwells_to_ohms = lambda e: (e**-e**2) * e**2
add(maxwells_to_ohms, 'maxwells', 'ohms')
print(convert('maxwells', 'ohms', 120))
