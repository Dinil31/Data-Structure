class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("enqueue to a full queue")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        item = self.queue[self.front]
        self.queue[self.front] = None  # Optional: clear the slot
        if self.front == self.rear:
            self.front = self.rear = -1  # Queue is now empty
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.queue[self.front]

    def get_size(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "CircularQueue: []"
        items = []
        i = self.front
        while True:
            items.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        return f"CircularQueue: {items}"

# Example usage
circular_queue = CircularQueue(3)
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
print(circular_queue)  # Output: CircularQueue: [1, 2, 3]
try:
    circular_queue.enqueue(4)  # Raises OverflowError
except OverflowError as e:
    print(e)

print(circular_queue.dequeue())  # Output: 1
print(circular_queue)  # Output: CircularQueue: [None, 2, 3]
circular_queue.enqueue(4)
print(circular_queue)  # Output: CircularQueue: [4, 2, 3]
print(circular_queue.peek())  # Output: 2
print(circular_queue.dequeue())  # Output: 2
print(circular_queue.dequeue())  # Output: 3
print(circular_queue.dequeue())  # Output: 4
try:
    circular_queue.dequeue()  # Raises IndexError
except IndexError as e:
    print(e)
