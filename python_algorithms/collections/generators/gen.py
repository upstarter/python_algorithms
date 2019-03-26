# Generators are a special class of functions that simplify the task of writing
# iterators. Regular functions compute a value and return it, but generators
# return an iterator that returns a stream of values.

# Here’s the simplest example of a generator function:

def generate_ints(N):
    for i in range(N):
        yield i


# Initialize a list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
a = (x**2 for x in my_list)

# Output: 1
print(next(a))

# Output: 9
print(next(a))

# Output: 36
print(next(a))

# Output: 100
print(next(a))

# Output: StopIteration
next(a)

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)

sum(x**2 for x in my_list)

max(x**2 for x in my_list)

class PowTwo:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

# This was lengthy. Now lets do the same using a generator function.

def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

# Pipelining
with open('sells.log') as file:
    pizza_col = (line[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x != 'N/A')
    print("Total pizzas sold = ",sum(per_hour))


# A generator function will be more clear if the generated
# expressions are more complex, involve multiple steps, or depend on additional
# temporary state.

# Consider the following example:

def unique(iterable, key=lambda x: x):
    seen = set()
    for elem, ekey in ((e, key(e)) for e in iterable):
        if ekey not in seen:
            yield elem
            seen.add(ekey)

# Here, the temporary keys collector, seen, is a temporary storage that will
# just be more clutter in the location where this generator will be used.

# Even if we were to use this only once, it is worth writing a function (for the
# sake of clarity; remember that Python allows nested functions).

# you can feed generators as input to other generators, creating long,
# data-driven pipelines, with sequence items pulled and processed as needed.


# The for...in clauses contain the sequences to be iterated over. The sequences do
# not have to be the same length, because they are iterated over from left to
# right, not in parallel. For each element in sequence1, sequence2 is looped over
# from the beginning. sequence3 is then looped over for each resulting pair of
# elements from sequence1 and sequence2.

seq1 = 'abc'
seq2 = (1,2,3)
[(x,y) for x in seq1 for y in seq2]
[('a', 1), ('a', 2), ('a', 3),
 ('b', 1), ('b', 2), ('b', 3),
 ('c', 1), ('c', 2), ('c', 3)]
