class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return {"data": self.data}

    def __str__(self):
        return "Node(data=" + str(self.data) + ", next=" + str(self.next)

    def search_list(N: Node, key: int) -> ListNode:
        while L and L.data != key:
            L = L.next
        # if key not in list, L is null
        return L

    def insert_after(node: ListNode, new_node: ListNode) -> None:
        new_node.next = node.next
        node.next = new_node

    def delete_after(node: ListNode) -> None:
        node.next = node.next.next


def reverse(head):
    prev, current = None, head
    while current is not None:
        # Make current node point to prev and move both forward one.
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


ll = Node(1, Node(2))
print(ll)
print(reverse(ll))
