# In this case we will try to print the linked list using a function insted of accessing them manually 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next

head = Node(10)
head.next = Node(30)
head.next.next = Node(50)

print_linked_list(head) # Here in this case we are accessing the linked list using a function
