# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

class Convert:

    kilos_to_pounds = lambda p: 2.20462  * p
    pounds_to_kilos = lambda k: 0.453592 * k
    pounds_to_grams = lambda p: p / 1000
    kilos_to_grams = lambda k: k * 1000
    meters_to_feet = lambda m: 3.28084 * m
    feet_to_meters = lambda f: 0.3048 * f
    farenheit_to_celsius = lambda f: (f - 32.0) * (5.0/9.0)
    celsius_to_farenheit = lambda c: (c * 9.0/5.0) + 32.0

    def __call__(cls, *args, **kwargs):
        cls.thismodule = cls
        print(cls.thismodule)

    whitelist = {
        'pounds': 'kilos',
        'kilos': 'pounds',
        'meters': 'feet',
        'feet': 'meters',
        'farenheit': 'celsius',
        'celsius': 'farenheit',
        'volts': 'gigavolts'
    }
    def is_allowed(self, source, dest):
        print(self.__class__.__name__)
        allowed = {
            source: self.whitelist.get(source, None)
            for k,v in self.whitelist.items()
            if source in self.whitelist and self.whitelist[source] == v
        }

        if not allowed:
            raise Exception(f'Cannot convert {source} to {dest}.')
        return True

    def add(self, func, source, dest):
        if self.is_allowed(source, dest):
            setattr(Convert.thismodule, '{}_to_{}'.format(source, dest), func)
            return True
        return False

    def convert(self, source, dest, value):
        if self.is_allowed(source, dest):
            val = getattr(Convert.thismodule, f'{source}_to_{dest}')(value)
            return val
        return None

print(Convert().convert('pounds', 'kilos', 10.0) == 4.53592)
print(Convert().convert('kilos', 'pounds', 10.0) == 22.0462)
print(Convert().convert('kilos', 'grams', 10.0) == 10_000)
print(Convert().convert('pounds', 'grams', 10.0) == 4535.92)
print(Convert().convert('meters', 'feet', 10.0) == 32.8084)
print(Convert().convert('feet', 'meters', 10.0) == 3.048)
print(round(Convert().convert('farenheit', 'celsius', 10.0), 2) == -12.22)
print(Convert().convert('celsius', 'farenheit', 10.0) == 50.0)

volts_to_gigavolts = lambda v: v * 0.000000001
add(volts_to_gigavolts, 'volts', 'gigavolts')
print(Convert().convert('volts', 'gigavolts', 100))


maxwells_to_ohms = lambda e: (e**-e**2) * e**2
add(maxwells_to_ohms, 'maxwells', 'ohms')
print(Convert().convert('maxwells', 'ohms', 120))
