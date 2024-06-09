
from collections import deque

# Define the Stack class
class Stack:
    def __init__(self):
        # Create an empty dequeue
        self.dequeue = deque()

    def push(self, item):
        # Append the item to the end of the dequeue
        self.dequeue.append(item)

    def pop(self):
        # Remove and return the item from the end of the dequeue
        return self.dequeue.pop()
    
    def size(self):
          # Return size of dequeue
        return len(self.dequeue)

    def is_empty(self):
        # Return True if the dequeue is empty, and False otherwise
        return not self.dequeue

    def top(self):
        # Return the item at the top of the stack without removing it.
        if self.is_empty():
            # If the stack is empty, return None
            return None
        else:
            # Return the last item in the dequeue
            return self.dequeue[-1]

if __name__ == '__main__':
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print("current size:", st.size())
    print(st.top())
    st.pop()
    print(st.top())
    st.pop()
    print(st.top())
    print("current size:", st.size())
