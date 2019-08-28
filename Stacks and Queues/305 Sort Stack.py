"""
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
"""
__author__ = 'abhireddy96'
from Stack import Stack



class SortedStack:
    def sort(self, stack):
        s = stack.copy()
        r = Stack()
        while not s.is_empty():
            tmp = s.pop()
            while not r.is_empty() and tmp > r.peek():
                s.push(r.pop())
            r.push(tmp)
        return r


if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(4)
    s.push(5)
    s.push(1)
    s.push(3)
    r = SortedStack().sort(s)
    s.print_stack()
    r.print_stack()




