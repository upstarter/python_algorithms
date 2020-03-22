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
