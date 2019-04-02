# Examples of iterators: range(), reversed()
# defined using generator functions

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch) # Outputs Node(1), Node(2)

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# Create the generator, notice no output appears
c = countdown(3)

print(next(c))
print(next(c))
print(next(c))
print(next(c)) # for loop takes care of except: StopIteration


## SLICING AND DICING
# take slice of an iterator
import itertools
for x in itertools.islice(c, 10, 20):
    print(x)

# Drop comments only at beginning of file, keep rest
from itertools import dropwhile
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

# however, if knowing the exact amount to drop
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

# finally, this will discard all comment lines
with open('/etc/passwd') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')

## ENUMERATION
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1):
    print(idx, val)

with open(filename, 'rt') as f:
    for lineno, line in enumerate(f, 1):
        fields = line.split
        try:
            print(lineno, line)
            count = int(fields[1])
        except ValueError as e:
            print('Line {}: Parse error: {}'.format(lineno, e))

# iterate over multiple sequences simultaneously
# length of iteration is length of shortest input
# replace with itertools.zip_longest() to avoid this
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x,y)

# iterating multiple containers efficiently
# Inefficent
# for x in a + b:
# Better
# for x in chain(a, b):
