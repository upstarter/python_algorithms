# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re


class Convert:

    whitelist = {
        "pounds": "kilos",
        "kilos": "pounds",
        "meters": "feet",
        "feet": "meters",
        "farenheit": "celsius",
        "celsius": "farenheit",
        "volts": "gigavolts",
    }

    kilos_to_pounds = lambda self, p: 2.20462 * p
    pounds_to_kilos = lambda self, k: 0.453592 * k
    pounds_to_grams = lambda self, p: p / 1000
    kilos_to_grams = lambda self, k: k * 1000
    meters_to_feet = lambda self, m: 3.28084 * m
    feet_to_meters = lambda self, f: 0.3048 * f
    farenheit_to_celsius = lambda self, f: (f - 32.0) * (5.0 / 9.0)
    celsius_to_farenheit = lambda self, c: (c * 9.0 / 5.0) + 32.0

    # can do this also:
    def __init__(self):
        self.y_to_z = lambda x: x - x

    def is_allowed(self, source, dest):
        allowed = {
            source: self.whitelist.get(source, None)
            for k, v in self.whitelist.items()
            if source in self.whitelist and self.whitelist[source] == v
        }

        if not allowed:
            raise Exception(f"Cannot convert {source} to {dest}.")
        return True

    def add(self, func, source, dest):
        if self.is_allowed(source, dest):
            setattr(self, "{}_to_{}".format(source, dest), func)
            return True
        return False

    def convert(self, source, dest, value):
        if self.is_allowed(source, dest):
            val = getattr(self, "{}_to_{}".format(source, dest))(value)
            return val
        return None


# note: none of these numbers are `100% accurate or precise`
converter = Convert()
print(converter.convert("pounds", "kilos", 10.0) == 4.53592)
print(converter.convert("kilos", "pounds", 10.0) == 22.0462)
print(converter.convert("kilos", "grams", 10.0) == 10_000)
print(converter.convert("pounds", "grams", 10.0) == 4535.92)
print(converter.convert("meters", "feet", 10.0) == 32.8084)
print(converter.convert("feet", "meters", 10.0) == 3.048)
print(round(converter.convert("farenheit", "celsius", 10.0), 2) == -12.22)
print(converter.convert("celsius", "farenheit", 10.0) == 50.0)

volts_to_gigavolts = lambda v: v * 0.000000001
converter.add(volts_to_gigavolts, "volts", "gigavolts")
print(converter.convert("volts", "gigavolts", 100))


maxwells_to_ohms = lambda Convert, e: (e ** -(e ** 2)) * e ** 2
converter.add(maxwells_to_ohms, "maxwells", "ohms")
print(converter.convert("maxwells", "ohms", 120))
