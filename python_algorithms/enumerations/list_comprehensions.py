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
