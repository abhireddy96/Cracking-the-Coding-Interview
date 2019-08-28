"""
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
push, pop and min should all operate in 0(1) time.

Solution:
1. Keep track of the minimum at each state(each operation).
2. Each node record what the minimum beneath itself is.
(When you push an element onto the stack, the element is given the current minimum)
"""
__author__ = 'abhireddy96'
import sys


class MinStack:
    def __init__(self):
        self.array = list()
        self.minValue = sys.maxsize  # Too keep track of min value

    def __str__(self):
        return ' '.join([str(x) for x in self.array])

    def min(self):
        return self.minValue

    def push(self, item):
        # If item is less than current minimum value of stack
        if item < self.minValue:
            self.minValue = item
        # If item is not less than minimum value of stack
        self.array.append(item)
        self.array.append(self.minValue)

    def pop(self):
        # Check if stack is empty
        if not self.array:
            return -1
        # Remove top element which is minimum value
        minVal = self.array.pop()
        # Again Remove top element which is actual value
        item = self.array.pop()
        # If popped min is minimum value of stack
        if minVal <= self.minValue:
            # Assign current top to minimum value
            self.minValue = self.array[-1]
        return item

    def peek(self):
        if not self.array:
            return -1
        return self.array[-2]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(3)
    print(stack)
    print(stack.peek())
    stack.push(2)
    print(stack)
    print(stack.min())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    stack.push(4)
    print(stack)
