rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},

]

# Now suppose you want to iterate over the data in chunks grouped by date.
# To do it, first sort by the desired field (in this case, date) and then use
# itertools.groupby():
from operator import itemgetter
from itertools import groupby
# Sort by the desired field first
rows.sort(key=itemgetter('date')) #
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)


## INVERT A DICT
# invert in order to perform calculations, also precendence sorting
prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }

# invert k,v using zip
inverted = zip(prices.values(), prices.keys())
print('inverted: {}'.format(inverted))
min_price = min(inverted)
print(min_price)

# rank data
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print('sorted: {}'.format(prices_sorted))


#When doing these calculations, be aware that zip() creates an iterator that can
#only be consumed once. For example, the following code is an error:

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
# OK
print(max(prices_and_names))
# ValueError: #max() arg is an empty sequence
