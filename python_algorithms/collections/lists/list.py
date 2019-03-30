from pprint import pprint
import itertools

data = [ 'OCN', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
name
#=> 'OCN'
date
#=> (2012, 12, 21)

name, shares, price, (year, mon, day) = data
name
# 'OCN'
year
#=> 2012
mon
#=> 12
day
#=> 21

list_num = [1,2,45,6,7,2,90,23,435]
list_char = ['c','o','o','k','i','e']

list_num.append(11) # Add 11 to the list, by default adds to the last position
print(list_num)

list_num.insert(0, 11)
print(list_num)

list_char.remove('o')
print(list_char)

list_char.pop(-2) # Removes the item at the specified position
print(list_char)

list_num.sort() # In-place sorting
print(list_num)

list.reverse(list_num)
print(list_num)

# flattening
a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))
# Output: [1, 2, 3, 4, 5, 6]
# or
print(list(itertools.chain(*a_list)))
# Output: [1, 2, 3, 4, 5, 6]
