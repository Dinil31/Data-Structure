class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if not self.head:
            return

        current_node = self.head
        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node:
            if current_node.prev:
                current_node.prev.next = current_node.next
            if current_node.next:
                current_node.next.prev = current_node.prev
            if current_node == self.head:
                self.head = current_node.next
            current_node = None

    def find(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def print_list_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def print_list_backward(self):
        current_node = self.head
        while current_node and current_node.next:
            current_node = current_node.next
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev
        print("None")

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    dll.print_list_forward()  # Output: 0 <-> 1 <-> 2 <-> 3 <-> None
    dll.delete_with_value(2)
    dll.print_list_forward()  # Output: 0 <-> 1 <-> 3 <-> None
    print(dll.find(3))  # Output: True
    print(dll.find(2))  # Output: False
    dll.print_list_backward()  # Output: 3 <-> 1 <-> 0 <-> None
