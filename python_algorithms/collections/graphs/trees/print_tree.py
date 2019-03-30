
import math
import numpy as np
from collections import defaultdict

def get_children(array_tree):
    return lambda i : [array_tree[2*i], array_tree[2*i+1]]

scores = [1, 3, 0, 7, 10, 3, 21, 21, 23, 32, 44, 55, 59, 62, 68, 72]

# import pdb; pdb.set_trace()
def print_tree():
    children = get_children(scores[1:])
    graph = defaultdict(list)
    # print('Len:', len(scores[1:]), scores[1:])

    for i in range(len(scores)-1):
        # depth = math.frexp(i+1)[1] # faster log base 2
        depth = int(math.floor(math.log(i+1, 2))) + 1
        try:
            graph[depth] += children(i)
        except IndexError:
            try:
                graph[depth] += [scores[1:][2*i]]
            except IndexError:
                None

    print('Depth 0:', scores[0])
    for depth, children in graph.items():
        print('Depth', depth, end=': ')
        print(children)

print_tree()

# In an array representation of a tree:
#
# if node: i
#
# Child: 2*i, 2*i+1

# Parent: i/2
