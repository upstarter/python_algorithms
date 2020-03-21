# For classes that primarily serve as simple data structures, you can often
# greatly reduce the memory footprint of instances by adding the __slots__
# attribute to the class definition.
class Date:
    __slots__ = ["year", "month", "day"]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
