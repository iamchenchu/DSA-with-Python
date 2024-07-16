# array can be implemented using the lists, or the array module that is built into Python, or the NumPy module.

# The array module is a built-in module in Python used to store arrays of a single data type.
# The array module defines a sequence data type that looks very much like a list, except that all of the members have to be of the same type.

class Myarray:
    def __init__(self): 
        self.array = []

    def insert(self, index, value):
        self.array.insert(index, value)
    
    def delete(self, index):
        self.array.pop(index)
    
    def update(self, value, index):
        self.array[index] = value
    
    def access(self, index):
        return self.array[index]
    
    def display(self):
        for e in self.array:
            print(e)


array = Myarray()
array.insert(0, 10)
array.insert(1, 55)
array.insert(2, 30)
array.display()
print(array.access(2))
