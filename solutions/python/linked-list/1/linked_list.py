class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.succeeding = new_node
            self.tail = new_node
        self.length += 1
        
    def pop(self):
        if self.tail is None:
            raise IndexError("List is empty")
        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail is not None:
            self.tail.succeeding = None
        else:
            self.head = None
        self.length -= 1
        return value

    def shift(self):
        if self.head is None:
            raise IndexError("List is empty")
        value = self.head.value
        self.head = self.head.succeeding
        if self.head is not None:
            self.head.previous = None
        else:
            self.tail = None
        self.length -= 1
        return value

    def unshift(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.succeeding = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def delete(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                break
            current = current.succeeding
        
        if current is None:
            raise ValueError("Value not found")
        
        if current.previous is not None:
            current.previous.succeeding = current.succeeding
        else:
            self.head = current.succeeding
        
        if current.succeeding is not None:
            current.succeeding.previous = current.previous
        else:
            self.tail = current.previous
        
        self.length -= 1
    
    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.succeeding
        
    
    
    
    
    
    
    
    
             