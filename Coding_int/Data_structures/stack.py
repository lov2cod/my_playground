
from Coding_int.Data_structures.node import Node


class Stack:

    def __init__(self, limit=1000):
        self.size = 0
        self.limit = limit
        self.top_item = None

    def push_item(self, value):
        if self.size < self.limit:
            new_item = Node(value)
            new_item.next_node = self.top_item
            self.top_item = new_item
            self.size += 1
        else:
            print("No space")

    def pop_item(self):
        if self.size < self.limit:
            current_node = self.top_item
            self.top_item = current_node.get_next_node()
            self.size -= 1
            return current_node.get_value()
        print("No items available")

    def peek(self):
        if self.size < self.limit:
            return self.top_item.get_value()
        print("No items available")
