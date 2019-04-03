from functools import partial
from functools import reduce

from itertools import count, islice, tee, repeat, cycle, chain, accumulate

def take(n, it):
    return [x for x in islice(it, n)]

def drop(n, it):
    return islice(it, n, None)

head = next

tail = partial(drop, 1)

def iterate(f, x):
    return accumulate(repeat(x), lambda fx, _: f(fx))


# use * and ** together or seperately for any number of positional and
# keyword args respectively. Both must be last in args list.
# For example:
def anyargs(*args, **kwargs):
    print(args) # A tuple
    print(kwargs) # A dict

# give useful hints to others
def add(x:int, y:int) -> int:
    return x + y

# Third-party tools and frameworks might also attach se‐mantic meaning to the
# annotations. They also appear in documentation:

#>>> help(add)
#=> Help on function add in module __main__:
#=> add(x: int, y: int) -> int

# multiple values
def myfun():
    return 1, 2, 3
a, b, c = myfun()

# If the default value is supposed to be a mutable container, such as a list,
# set, or dictionary, use None as the default and write code like this:
# Using a list as a default value:
def container_default_arg(a, b=None):
    if b is None:
        b = []

_no_value = object()
def arg_test(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    else:
        print(b)

arg_test(1)
#=> No b value supplied
arg_test(1, 2) # b = 2
arg_test(1,None) # b = None
