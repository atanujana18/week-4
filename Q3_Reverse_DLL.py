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
def reverse():
    global head
    temp = None
    current = head
    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    if temp:
        head = temp.prev
def display():
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
insert(3); insert(2); insert(1)
reverse()
display()