from collections import deque

class DequeUsingTwoQueues:
    def __init__(self):
        self.q1 = deque()  # Queue for front operations
        self.q2 = deque()  # Queue for rear operations
    
    def is_empty(self):
        return not self.q1 and not self.q2

    def add_front(self, item):
        self.q1.append(item)
    
    def add_rear(self, item):
        self.q2.append(item)
    
    def remove_front(self):
        if self.q1:
            return self.q1.pop()
        elif self.q2:
            while len(self.q2) > 1:
                self.q1.appendleft(self.q2.popleft())
            return self.q2.popleft()
        else:
            raise IndexError("remove_front from an empty deque")
    
    def remove_rear(self):
        if self.q2:
            return self.q2.pop()
        elif self.q1:
            while len(self.q1) > 1:
                self.q2.appendleft(self.q1.popleft())
            return self.q1.popleft()
        else:
            raise IndexError("remove_rear from an empty deque")
    
    def size(self):
        return len(self.q1) + len(self.q2)
    
    def peek_front(self):
        if self.q1:
            return self.q1[-1]
        elif self.q2:
            while len(self.q2) > 1:
                self.q1.appendleft(self.q2.popleft())
            front = self.q2.popleft()
            self.q1.appendleft(front)
            return front
        else:
            raise IndexError("peek_front from an empty deque")
    
    def peek_rear(self):
        if self.q2:
            return self.q2[-1]
        elif self.q1:
            while len(self.q1) > 1:
                self.q2.appendleft(self.q1.popleft())
            rear = self.q1.popleft()
            self.q2.appendleft(rear)
            return rear
        else:
            raise IndexError("peek_rear from an empty deque")

# Example usage
deque = DequeUsingTwoQueues()
deque.add_rear(1)
deque.add_rear(2)
deque.add_front(0)
print(deque.remove_front())  # Output: 0
print(deque.remove_rear())   # Output: 2
print(deque.size())          # Output: 1
