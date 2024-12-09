class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, item):
        if self.head:

            pointer = self.head
            while(pointer.next):
                pointer = pointer.next

            pointer.next = Node(item)
        else:
            self.head = Node(item)
        self._size = self._size + 1

    def __len__(self):
        return self._size
    
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def set(self):
        pass

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")
        
    def _setitem(self, index, item):
        pointer = self._getnode(index)
        if pointer:
                pointer.data  = item
        else:
            raise IndexError("list index out of range")
        
    def index(self, item):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == item:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError("{} is not in list".format(item))
    
lista = SingleLinkedList()
lista.append(9)
print(lista.size)