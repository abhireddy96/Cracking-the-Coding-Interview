"""
Implement an algorithm to delete a node in the middle (ie., any node but the first and last node,
not necessarily the exact middle) of a singly linked list, given only access to that node.
EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f

Solution:
1. Copy the data from the next node over to the current node, and then to delete the next node.
"""
__author__ = 'abhireddy96'
from LinkedList import LinkedList, LinkedListNode


class Solution:
    def deleteMiddleNode(self, node: LinkedListNode):
        # Reference next node to current node
        node.value = node.next.value
        node.next = node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middle = ll.add(5)
    ll.add_multiple([7, 8, 9])
    print(ll)
    Solution().deleteMiddleNode(middle)
    print(ll)




