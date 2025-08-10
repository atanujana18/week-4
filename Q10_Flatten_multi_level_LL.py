class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None
def merge(a, b):
    if not a: return b
    if not b: return a
    if a.data < b.data:
        a.next = merge(a.next, b)
        return a
    else:
        b.next = merge(a, b.next)
        return b
def flatten(root):
    if not root or not root.next:
        return root
    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root
def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
head = Node(5)
head.child = Node(7)
head.next = Node(10)
head = flatten(head)
print_list(head)