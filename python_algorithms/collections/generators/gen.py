# Initialize the list
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
