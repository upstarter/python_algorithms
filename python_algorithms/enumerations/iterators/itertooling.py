from itertools import chain, groupby
from itertools import islice, cycle
from itertools import combinations, permutations
from itertools import product, count, compress
from functools import reduce

# from itertools import ifilter
# from itertools import imap
# from itertools import izip

## groupby
mylist = "aaaaabbbbbccdd"  # sorted
# group returns a generator
print(list(groupby(mylist)))

# to extract from the generator groups
print({k: list(v) for k, v in groupby(mylist)})


mylist = [
    {"group": 1, "name": "ray"},
    {"group": 1, "name": "jeremy"},
    {"group": 3, "name": "grant"},
]
print({k: list(v) for k, v in groupby(mylist, key=lambda x: x["group"])})


mylist = [
    {"id": 1, "name": "ray"},
    {"id": 1, "email": "ray@hotmail.com"},
    {"id": 2, "name": "liz"},
    {"id": 2, "email": "liz@hotmail.com"},
]

# map name, email to id
res = [
    dict(
        reduce(
            lambda y, z: y | z,  # entries union
            map(lambda x: x.items(), v),  # x is a grouper items object generator
        )
    )
    for k, v in groupby(mylist, key=lambda x: x["id"])
]

print(res)


## SLICING AND DICING
# take slice of an iterator
for x in islice(range(1, 20), 1, 2):
    print(x)

# like a circulary linked list
# if list large, memory intensive
orbit = cycle("12345678")
print([next(orbit) for i in range(0, 10)])

## Chain
a = [1, 2, 3]
b = range(9, 4)
print(list(chain(a, b)))

# flattening a matrix
a_list = [[1, 2], [3, 4], [5, 6]]
print(list(chain.from_iterable(a_list)))
# Output: [1, 2, 3, 4, 5, 6]
# or
print(list(chain(*a_list)))
# Output: [1, 2, 3, 4, 5, 6]

## compress
mylist = "abcdef"
myselectors = [1, 0, 1, 1, 0, 1]
print(list(compress(mylist, myselectors)))
# => ['a', 'c', 'd', 'f']

print([v for v, s in zip(mylist, myselectors) if s])
# => ['a', 'c', 'd', 'f']

# count
# do not call len or list on this
counter = count(1, 5)  # like stepper in closures.py
for c in "abc":
    print("".join(c))


# islice  knowing the exact amount to drop
items = ["a", "b", "c", 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

# iterate over multiple sequences simultaneously
# length of iteration is length of shortest input
# replace with itertools.zip_longest() to avoid this
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

# iterating multiple containers efficiently
# Inefficent
a, b = [[1, 2], [3, 4]]
for x in a + b:
    print(x)
# Better
for x in chain(a, b):
    print(x)

# Drop comments only at beginning of file, keep rest
# from itertools import dropwhile
# with open('/etc/passwd') as f:
#     for line in dropwhile(lambda line: line.startswith('#'), f):
#         print(line)

# finally, this will discard all comment lines
# with open('/etc/passwd') as f:
#     lines = (line for line in f if not line.startswith('#'))
#     for line in lines:
#         print(line)
