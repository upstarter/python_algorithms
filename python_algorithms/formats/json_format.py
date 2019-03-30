# python to json
import json
from urllib.request import urlopen

data = { 'name' : 'ACME', 'shares' : 100, 'price' : 542.23 }
json_str = json.dumps(data)


# Here is how you turn a JSON-encoded string back into a Python data structure:
data = json.loads(json_str)

# If you are working with files instead of strings, use
# json.dump() and json.load() to encode and decode JSON data.

# For example:

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)

# more sane pretty print
u = urlopen('http://search.twitter.com/search.json?q=rust&rpp=5')
resp = json.loads(u.read().decode('utf-8'))

from pprint import pprint
pprint(resp)

# keep order
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
