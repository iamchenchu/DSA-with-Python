# this is a simple linked list implementation
# a linked list is a collection of nodes where each node contains a value and a reference to the next node in the list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print(head.value)
print(head.next.value)
print(head.next.next.value)
