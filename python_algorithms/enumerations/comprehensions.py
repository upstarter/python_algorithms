## List Comprehensions
matrix = [[1,2,3], [4,5,6]]

# for loop
negative_matrix = []
for row in matrix:
    negative_matrix.append([-n for n in row])

# list comprehension
negative_evens_matrix = [
    [-n for n in row] # or negate(n)
    for row in matrix
    if n % 2 == 0
]

from itertools import izip
list(zip(*matrix)) # returns tuples
print([list(col) for col in izip(*matrix)])

# Dict Comprehension
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = {k + '_key': v * 2 for k,v in my_dict.iteritems()}
print(result)
print(result.iterkeys())
print(result.itervalues())
print(result.iteritems())
