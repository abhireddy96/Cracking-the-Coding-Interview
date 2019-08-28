"""
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
If x is contained within the list, the values of x only need to be after the elements less than x (see below).
The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -) 5 -) 8 -) 5 -) 113 -) 2 -) 1 [partition = 5]
Output: 3 -) 1 -) 2 -) 113 -) 5 -) 5 -) 8

Solution:

1. Create a "res" list (using the existing nodes).
2. Elements bigger than the pivot element are put at the tail.
3. Elements smaller are put at the head.
(Each time we insert an element, we update either the head or tail)
"""
__author__ = 'abhireddy96'
from LinkedList import LinkedList


class Solution:
    def partition(self, ll, x):
        current = ll.tail = ll.head

        while current:
            # Store node and unlink it
            nextNode = current.next
            current.next = None
            # If current value < x , make it head
            if current.value < x:
                current.next = ll.head
                ll.head = current
            # if not append it to tail
            else:
                ll.tail.next = current
                ll.tail = current
            current = nextNode

        # Error check in case all nodes are less than x
        if ll.tail.next is not None:
            ll.tail.next = None


if __name__ == "__main__":
    ll = LinkedList()
    ll.generate(10, 0, 99)
    print(ll)
    Solution().partition(ll, ll.head.value)
    print(ll)




