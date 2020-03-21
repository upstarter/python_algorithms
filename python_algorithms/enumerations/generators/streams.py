# Infinite Stream Representation
# The following example can generate all the even numbers (at least in theory).


def all_even():
    n = 0
    while True:
        yield n
        n += 2
