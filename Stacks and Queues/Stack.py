class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        old_top = self.top
        self.top = old_top.next
        return old_top.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def copy(self):
        s = Stack()
        x = self.top
        while x:
            s.push(x.data)
            x = x.next
        return s

    def print_stack(self):
        x = self.top
        while x:
            print(x.data, "-> ", end="")
            x = x.next
        print(None)

