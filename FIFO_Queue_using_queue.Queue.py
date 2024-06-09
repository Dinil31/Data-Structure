import queue

class ThreadSafeQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def enqueue(self, item):
        self.queue.put(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.get()
        raise IndexError("Dequeue from an empty queue")

    def is_empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()

# Example usage
tsq = ThreadSafeQueue()
tsq.enqueue(1)
tsq.enqueue(2)
tsq.enqueue(3)
print(tsq.dequeue())  # Output: 1
print(tsq.dequeue())  # Output: 2
print(tsq.dequeue())  # Output: 3
