class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
head = None
def insert(data):
    global head
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    head = new_node
def delete_node(node):
    global head
    if not head or not node:
        return
    if head == node:
        head = node.next
    if node.next:
        node.next.prev = node.prev
    if node.prev:
        node.prev.next = node.next
def display():
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
insert(3); insert(2); insert(1)
display()
delete_node(head.next)
print()
display()