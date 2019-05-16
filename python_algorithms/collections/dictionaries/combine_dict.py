a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
# Outputs 1 (from a)
print(c['y'])
# Outputs 2 (from b)
print(c['z'])


# by hand based on rules
from itertools import groupby
mylist = [
    { 'id': 1, 'name': 'ray' },
    { 'id': 1, 'email': 'ray@hotmail.com' },
    { 'id': 2, 'name': 'liz' },
    { 'id': 2, 'email': 'liz@hotmail.com' }
]

from functools import reduce
# map name, email to id
res = [ dict(
    reduce(lambda y, z: y | z, # entries union
      map(lambda x: x.items(), v) # x is a grouper items object generator
    )
) for k, v in groupby(mylist, key=lambda x: x['id']) ]

print(res)
