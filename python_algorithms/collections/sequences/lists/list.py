from pprint import pprint

# Membership
all(x in ["b", "a", "foo", "bar"] for x in ["a", "b"])
# => True

# Manipulation
list_num = [1, 2, 45, 6, 7, 2, 90, 23, 435]
list_char = ["c", "o", "o", "k", "i", "e"]

# returns smallest index i, where s[i] == 2.
# Can include start,stop index for lookup
list_num.index(2, 2, -1)
# => 5

list_char.pop(-2)  # Removes the item at the specified position
print (list_char)

list_char.remove("o")
print (list_char)

list_num.sort()  # In-place sorting
print (list_num)

list.reverse(list_num)
print (list_num)

list_num.append(11)  # Add 11 to the list, by default adds to the last position
print (list_num)

list_num.extend([11, 44])  # Add 11 and 44 to end of the list
print (list_num)

list_num.count(2)  # count occurrences of 2. 2 appears twice
# => 2

list_num.insert(0, 11)
print (list_num)

# ON ABOVE: ANYWHERE YOU SEE THIS, USE A DEQUE INSTEAD OF LIST(inefficient)
del names[0]
names.pop(0)
names.insert(0, "mark")

names = deque(["ray", "rachel", "charlie"])

# NOW CAN OPERATE EFFICIENTLY
del names[0]
names.popleft()
names.appendleft("mark")

# Destructuring/Unpacking sequences
data = ["OCN", 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name
# => 'OCN'
date
# => (2012, 12, 21)

name, shares, price, (year, mon, day) = data
name
# 'OCN'
year
# => 2012
mon
# => 12
day
# => 21


# UPDATING MULTIPLE STATE VARIABLES
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print x
        x, y = y, x + y
