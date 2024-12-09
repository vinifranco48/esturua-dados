class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, item):
       
    def pop(self):
       
        raise IndexError('The stack is empty')


    def peek(self):
        if self._size > 0:
            return self.top
        raise IndexError('The stack is empty')

    def __len__(self):
        return self._size
    
    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()