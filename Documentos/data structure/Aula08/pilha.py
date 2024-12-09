class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self._size = self._size + 1
    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node
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
    
pilha = Stack()
pilha.push(1)
pilha.push(2)
pilha.push(4)

print(pilha)
