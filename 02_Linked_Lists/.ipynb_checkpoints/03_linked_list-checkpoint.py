# In this program we will try to create a linked list using a function
# also access the linked list using a function

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(input_list): # Here we are creating a linked list using a function
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
            current = head
        else:
            current.next = Node(value)
            current = current.next
    return head

def print_linked_list(head): # Here we are accessing the linked list using a function
    current = head
    while current is not None:
        print(current.value)
        current = current.next

head = create_linked_list([10, 20, 30, 40, 50]) # Here we are creating a linked list using a function
print_linked_list(head) # Here we are accessing the linked list using a function