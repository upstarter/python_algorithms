# Dict - fundamental tool: relations, linking, counting, grouping


d = {"a": 1, "b": 2}

# ITERATE ON KEYS (DEFAULT LOOPING BEHAVIOR)
for k in d:
    print(k)

# MUTATION WHILE LOOPING
# BUT: if you want to mutate what your iterating over
# note: if you mutate while iterating your living in sin and deserve whatever happens to you
for k in d.keys():
    if k.startswith("r"):
        del d[k]

# d.items() returns a generator (itemview)
for k, v in d.items():
    print(k, v)

# CONSTRUCT A DICT FROM PAIRS
names = ["ray", "rachel"]
colors = ["red", "green"]

d = dict(zip(names, colors))
# izip_longest fills in None's for the shortest collection

# correspondence relations
res = zip("abcd", "wxyz")
print("res", dict(res))
# => {'a': 'w', 'b': 'x', 'c': 'y', 'd': 'z'}

print(dict([(k * 3, v) for k, v in res]))

print(dict(enumerate(names)))
# => {0: 'ray', 1: 'rachel'}

# COUNTING WITH DICTS
d = defaultdict(int)
for color in colors:
    d[color] += 1

# GROUPING WITH DICTS
from collections import defaultdict

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)


# to convert a list of tuples to a dictionary using the first value as the key.
# Looked like this (making a database of comic book files):
data = [
    ((31), ("Amazing Spider-Man"), (481), ("Marvel")),
    ((28), ("The Incredible Hulk"), (612), ("Marvel")),
]  # etc, hundreds more like this.

# could have done this:
dict_data = {}
for i in data:
    dict_data[i[0]] = [i[1], i[2], i[3]]

# a more Pythonic approach.
# dict_data = {i[0]:[*i[1:]] for i in data}
# print(dict_data)
