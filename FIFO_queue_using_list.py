class ListQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage
lq = ListQueue()
lq.enqueue(1)
lq.enqueue(2)
lq.enqueue(3)
print(lq.dequeue())  # Output: 1
print(lq.dequeue())  # Output: 2
print(lq.dequeue())  # Output: 3
