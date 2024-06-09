from collections import deque

class DequeQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("Dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage
dq = DequeQueue()
dq.enqueue(1)
dq.enqueue(2)
dq.enqueue(3)
print(dq.dequeue())  # Output: 1
print(dq.dequeue())  # Output: 2
print(dq.dequeue())  # Output: 3
