from itertools import groupby
mylist = [
    { 'id': 1, 'name': 'ray' },
    { 'id': 1, 'email': 'ray@hotmail.com' },
    { 'id': 2, 'name': 'liz' },
    { 'id': 2, 'email': 'liz@hotmail.com' }
]

# map name, email to id
res = [ dict(
    reduce(lambda y, z: y + z, # sum works too!
      map(lambda x: x.items(), v) # x is a tuple of k,v
    )
) for k, v in groupby(mylist, key=lambda x: x['id']) ]

print(res)
