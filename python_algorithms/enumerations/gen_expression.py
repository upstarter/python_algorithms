# Initialize a list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x ** 2 for x in my_list]

# same thing can be done using generator expression,
# while loading each element into memory as needed
# instead of loading the whole array into memory
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
a = (x ** 2 for x in my_list)

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
