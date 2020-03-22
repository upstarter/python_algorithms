# In general, you should use a for loop when you know how many times the loop
# should run. If you want the loop to break based on a condition other than the
# number of times it runs, you should use a while loop.

# Looping over a range of numbers (all 3 below are same use iterator protocol)
for i in [0, 1, 2, 3]:
    print(i ** 2)

for i in range(6):
    print(i ** 2)

# in python 2 xrange is a generator
for i in range(6):
    print(i ** 2)

# Looping over a collection
colors = ["red", "green"]

# NOT SO GOOD if you don't need an index
for i in range(len(colors)):
    print(colors[i])

# BETTER
for color in colors:
    print(color)

# looping over a collection with index
for i, color in enumerate(colors):
    print(i, "-->", colors[i])

# Looping in sorted order
for color in sorted(colors, reverse=True):
    print(color)

# in reverse
for color in reversed(colors):
    print(color)

# sort by length
print(sorted(colors, key=len))

# Looping over two collections at once
names = ["ray", "rachel"]
for name, color in zip(names, colors):
    print(name, "-->", color)

# Distinguishing multiple exit points in loops
# NOT SO GOOD
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i


# GOOD, knuth's idea
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    # `for` has an implicit `if` underneath (if i haven't finish body)
    # finished body, normal return does not hit, only the break
    else:
        return -1
    return i
