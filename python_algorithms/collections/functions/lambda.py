# Functional programming can be considered the opposite of object-oriented
# programming. Objects are little capsules containing some internal state along
# with a collection of method calls that let you modify this state, and programs
# consist of making the right set of state changes. Functional programming wants
# to avoid state changes as much as possible and works with data flowing between
# functions. In Python you might combine the two approaches by writing functions
# that take and return instances representing objects in your application
# (e-mail messages, transactions, etc.).
#
# Functional design may seem like an odd constraint to work under. Why should
# you avoid objects and side effects? There are theoretical and practical
# advantages to the functional style:
#
# Formal provability.
# Modularity.
# Composability.
# Ease of debugging and testing.

(lambda a, b: a + b)(3, 4)  # returns 7

addition = lambda a, b: a + b
addition(3, 4)  # returns 7

authors = ['John Von Neumann', 'Claude Shannon', 'Alan Turing', 'Carl Jung', 'John Nash', 'Benjamin Graham']
sort = sorted(authors, key=len)  # Returns list ordered by length of author name
print(sort)
sort = sorted(authors, key=lambda name: name.split()[-1])  # Returns list ordered alphabetically by last name.
print(sort)

from functools import reduce

val = [1, 2, 3, 4, 5, 6]

# Multiply every item by two
print(list(map(lambda x: x * 2, val))) # [2, 4, 6, 8, 10, 12]
# Take the factorial by multiplying the value so far to the next item
print(reduce(lambda x, y: x * y, val, 1)) # 1 * 1 * 2 * 3 * 4 * 5 * 6


x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
# What are the values of a(10) and b(10)?
# If you think the results might be 20 and 30, you would be wrong:
a(10)
#=> 30
b(10)
#=> 30

# If you want an anonymous function to capture a value at the point of definition
# and keep it, include the value as a default value, like this:
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
a(10)
#=> 20
b(10)
#=> 30
