"""
Describe how you could use a single array to implement three stacks.

Solution:
Divide the array in three equal parts and allow the individual stack to grow in that limited space.
• For stack 1 -> 0 to n/3
• For stack 2 -> n/3 to 2n/3
• For stack 3 -> 2n/3 to n
"""
__author__ = 'abhireddy96'


class MultiStack:

    def __init__(self, stackSize):
        self.numofStacks = 3  # No. of stacks
        self.array = [0] * (stackSize * self.numofStacks)  # Initialize stack with zeros
        self.sizes = [0] * self.numofStacks  # Array to track stacks index n size
        self.stackSize = stackSize  # Size of each stack

    def __str__(self):
        stack1 = 'Stack1: ' + ' '.join([str(x) for x in self.array[0:self.stackSize]]) + '\n'
        stack2 = 'Stack2: ' + ' '.join([str(x) for x in self.array[self.stackSize: 2*self.stackSize]]) + '\n'
        stack3 = 'Stack3: ' + ' '.join([str(x) for x in self.array[2*self.stackSize:]])
        return stack1 + stack2 + stack3

    def Push(self, item, stackNum):
        # Check if particular stack is full
        if self.IsFull(stackNum):
            raise Exception('Stack is full')
        # Increase item count in particular in stack by 1
        self.sizes[stackNum] += 1
        # Fetch top index of particular stack n assign it with current value
        self.array[self.IndexOfTop(stackNum)] = item

    def Pop(self, stackNum):
        # Check if particular stack is empty
        if self.IsEmpty(stackNum):
            raise Exception('Stack is empty')
        # Fetch top index of particular stack n make value zero
        value = self.array[self.IndexOfTop(stackNum)]
        self.array[self.IndexOfTop(stackNum)] = 0
        # Reduce item count in particular in stack by 1
        self.sizes[stackNum] -= 1
        return value

    def Peek(self, stackNum):
        # Check if particular stack is empty
        if self.IsEmpty(stackNum):
            raise Exception('Stack is empty')
        # Fetch top index of particular stack n return it's value
        return self.array[self.IndexOfTop(stackNum)]

    def IsEmpty(self, stackNum):
        # Checks if particular stack is empty
        return self.sizes[stackNum] == 0

    def IsFull(self, stackNum):
        # Checks if particular stack is full
        return self.sizes[stackNum] == self.stackSize

    def IndexOfTop(self, stackNum):
        # Calculate offset or starting index of particular stack
        offset = stackNum * self.stackSize
        # Top index will be offset + last index of an element
        return offset + self.sizes[stackNum] - 1


if __name__ == "__main__":
    stack = MultiStack(2)
    print(stack.IsEmpty(1))
    stack.Push(3, 1)
    print(stack)
    print(stack.Peek(1))
    print(stack.IsEmpty(1))
    stack.Push(2, 1)
    print(stack)
    print(stack.Peek(1))
    print(stack.Pop(1))
    print(stack.Peek(1))
    stack.Push(3, 1)
    print(stack)




