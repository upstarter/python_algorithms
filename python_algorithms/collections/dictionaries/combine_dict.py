a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
# Outputs 1 (from a)
print(c['y'])
# Outputs 2 (from b)
print(c['z'])
