# HEAP AS A TREE ( PRIORITY QUEUE / MINHEAP / MAXHEAP )
# https://docs.python.org/2/library/heapq.html

# root of tree: first element (i = 1)
# parent(i) = i/2
# leaft(i) = 2i, right(i) = 2i + 1

# MaxHeap property:
# key of a node >= the keys of its children
# trivial max() operation, constant time, just find item i = 1

# MinHeap property:
# key of a node <= the keys of its children
