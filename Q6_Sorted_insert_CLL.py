class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
last = None
def sorted_insert(data):
    global last
    new_node = Node(data)
    if not last:
        last = new_node
        last.next = last
    elif data <= last.next.data:
        new_node.next = last.next
        last.next = new_node
    else:
        temp = last.next
        while temp.next != last.next and temp.next.data < data:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        if temp == last:
            last = new_node
def display():
    if not last:
        return
    temp = last.next
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == last.next:
            break
sorted_insert(2); sorted_insert(1); sorted_insert(3)
display()