# To change the string representation of an instance, define the __str__() and
# __repr__() methods.
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

# The __repr__()method returns the code representation of an instance, and is
# usually the text you would type to re-create the instance. The built-in repr()
# function returns this text, as does the interactive interpreter when
# inspecting values. The __str__() method converts the instance to a string, and
# is the output produced by the str() and print() functions.


# To customize string formatting, define the __format__() method on a class. For
# example:

_formats = { 'ymd' : '{d.year}-{d.month}-{d.day}', 'mdy' : '{d.month}/{d.day}/{d.year}', 'dmy' : '{d.day}/{d.month}/{d.year}' }

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)
