# Deques are a generalization of stacks and queues (the name is pronounced “deck”
# and is short for “double-ended queue”). Deques support thread-safe, memory
# efficient appends and pops from either side of the deque with approximately the
# same O(1) performance in either direction.

# UPDATING SEQUENCES
names = ["ray", "rachel", "charlie"]

# ANYWHERE YOU SEE THIS, USE A DEQUE INSTEAD OF LIST(inefficient)
del names[0]
names.pop(0)
names.insert(0, "mark")

names = deque(["ray", "rachel", "charlie"])

# NOW CAN OPERATE EFFICIENTLY
del names[0]
names.popleft()
names.appendleft("mark")
