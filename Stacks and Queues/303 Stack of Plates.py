"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.

Solution:
1. If the last stack is at capacity, then create a new stack.
2. If the last stack is empty (after popping), then remove the stack from the list of stacks.
"""
__author__ = 'abhireddy96'
from Stack import Stack


class SetOfStacks(object):

    def __init__(self, stack_capacity):
        self.stack_capacity = stack_capacity
        self.stacks = [Stack()]

    def push(self, data):
        if len(self.stacks) == 0 or self.stacks[-1].get_size() == self.stack_capacity:
            self.stacks.append(Stack())
        self.stacks[-1].push(data)

    def pop(self):
        if len(self.stacks) == 0:
            raise Exception("Stack is empty.")
        data = self.stacks[-1].pop()
        if self.stacks[-1].get_size() == 0:
            self.stacks.pop()
        return data

    # leave stacks half-full
    def popAtHalfFull(self, index):
        if len(self.stacks) == 0:
            raise Exception("Stack is empty.")
        if index > len(self.stacks) - 1:
            raise IndexError("Index out of range.")
        else:
            data = self.stacks[index].pop()
            if self.stacks[index].get_size() == 0:
                del self.stacks[index]
            return data

    # full implementation
    def popAt(self, index):
        if len(self.stacks) == 0:
            raise Exception("Stack is empty.")
        if index > len(self.stacks) - 1:
            raise IndexError("Index out of range.")
        else:
            data = self.stacks[index].pop()
            if self.stacks[index].get_size() == 0:
                del self.stacks[index]
            else:
                self.reorder_stacks(index)
            return data

    def reorder_stacks(self, index):
        while index < len(self.stacks) - 1:
            prev = None
            x = self.stacks[index+1].head
            if x.next:
                while x.next:
                    prev = x
                    x = x.next
                prev.next = x.next
            else:
                del self.stacks[index+1]
            self.stacks[index].push(x.data)
            index += 1

    def print_stack(self):
        i = len(self.stacks)
        while i > 0:
            stack = self.stacks[i-1]
            i -= 1
            x = stack.head
            while x:
                print(x.data, "-> ", end="")
                x = x.next
        print(None)


if __name__ == "__main__":
    stacks = SetOfStacks(5)
    for i in range(35):
        stacks.push(i)
    lst = []
    for _ in range(35):
        lst.append(stacks.pop())
