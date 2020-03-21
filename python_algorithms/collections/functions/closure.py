# Accessing variables
def example():
    n = 0

    # closure
    def func():
        print("n=", n)

    # Accessors
    def get_n():
        return n

    def set_n(val):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n
    return func


f = example()
f()
# => n=0
f.set_n(10)
f()
# => n=10
f.get_n()
# => 10

import sys


class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Update instance dictionary with callables
        self.__dict__.update(
            (key, value) for key, value in locals.items() if callable(value)
        )

    # Redirect special methods
    def __len__(self):
        return self.__dict__["__len__"]()


# Example use
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
s.push(10)
s.push(20)
s.push("Hello")
len(s)
# => 3
s.pop()
# => 'Hello'
