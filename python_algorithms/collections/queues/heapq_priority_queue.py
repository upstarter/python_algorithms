# demonstration of heapify(), heappush() and heappop()

from heapq import heappush, heappop

heap = []
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for item in data:
    heappush(heap, item)

ordered = []
while heap:
    ordered.append(heappop(heap))

ordered
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data.sort()
data == ordered
# True

# Using a heap to insert items at the correct place in a priority queue:
heap = []
data = [(1, "J"), (4, "N"), (3, "H"), (2, "O")]
for item in data:
    heappush(heap, item)

while heap:
    print(heappop(heap)[1])
