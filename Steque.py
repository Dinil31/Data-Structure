class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Steque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty steque")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return value

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

# Example usage
steque = Steque()
steque.push(1)
steque.push(2)
steque.enqueue(3)
print(list(steque))  # Output: [2, 1, 3]
print(steque.pop())  # Output: 2
print(list(steque))  # Output: [1, 3]
