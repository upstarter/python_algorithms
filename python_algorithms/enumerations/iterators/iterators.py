# Defined using generator functions
# Examples of iterators: range(), reversed()


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)  # Outputs Node(1), Node(2)

## Iteration
my_list = ["a", "b", "c"]
for idx, val in enumerate(my_list, 1):
    print(idx, val)

with open(filename, "rt") as f:
    for lineno, line in enumerate(f, 1):
        fields = line.split
        try:
            print(lineno, line)
            count = int(fields[1])
        except ValueError as e:
            print("Line {}: Parse error: {}".format(lineno, e))
