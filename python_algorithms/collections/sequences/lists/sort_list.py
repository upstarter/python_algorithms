from operator import itemgetter, attrgetter

sorted = sorted([1, 4, 3, 2])
print(sorted)

# Precedence Sort / Complex Sorts
# Starting with Python 2.2, sorts are guaranteed to be stable. That means that
# when multiple records have the same key, their original order is preserved.

data = [("red", 1), ("blue", 1), ("red", 2), ("blue", 2)]

# sorted(data, key=itemgetter(0))
# => [('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]

# Notice how the two records for blue retain their original order so that
# ('blue', 1) is guaranteed to precede ('blue', 2).

# Operator Module Functions
# The key-function patterns  are very common for sorting, so Python provides
# convenience functions to make accessor functions easier and faster. The
# operator module has operator.itemgetter(), operator.attrgetter(), and starting
# in Python 2.5 an operator.methodcaller() function.

# Using those functions, the above examples become simpler and faster:

student_tuples = [
    ("john", "A", 15),
    ("jane", "B", 12),
    ("dave", "B", 10),
]


sorted(student_tuples, key=itemgetter(2))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

sorted(student_tuples, key=attrgetter("age"))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# The operator module functions allow multiple levels of sorting. For example,
# to sort by grade then by age:

sorted(student_tuples, key=itemgetter(1, 2))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

sorted(student_tuples, key=attrgetter("grade", "age"))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

# The operator.methodcaller() function makes method calls with fixed parameters
# for each object being sorted. For example, the str.count() method could be used
# to compute message priority by counting the number of exclamation marks in a
# message:

from operator import methodcaller

messages = ["critical!!!", "hurry!", "standby", "immediate!!"]

sorted(messages, key=methodcaller("count", "!"))

# ['standby', 'hurry!', 'immediate!!', 'critical!!!']

# This wonderful property lets you build complex sorts in a series of sorting
# steps. For example, to sort the student data by descending grade and then
# ascending age, do the age sort first and then sort again using grade:

s = sorted(student_tuples, key=attrgetter("age"))  # sort on secondary key
sorted(s, key=attrgetter("grade"), reverse=True)  # now sort on primary key, descending
[("dave", "B", 10), ("jane", "B", 12), ("john", "A", 15)]
