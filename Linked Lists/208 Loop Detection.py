"""
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C - > D -> E -> C [the same C as earlier)
Output: C

Solution:
1. Create two pointers, FastPointer and SlowPointer.
2. Move FastPointer at a rate of 2 steps and SlowPointer at a rate of 1 step.
3. When they collide, move SlowPointer to LinkedListHead. Keep FastPointer where it is.
4. Move SlowPointer and FastPointer at a·rate of one step. Return the new collision point.
"""
__author__ = 'abhireddy96'
from LinkedList import LinkedList


class Solution:
    def loopDetection(self, ll):
        fast = slow = ll.head

        # Move FastPointer at a rate of 2 steps and SlowPointer at a rate of 1 step
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # Break on collision
            if fast is slow:
                break

        # If they don't collide
        if fast is None or fast.next is None:
            return None

        # Move SlowPointer and FastPointer at a·rate of one step.
        # Return the new collision point.
        slow = ll.head
        while fast is not slow:
            fast = fast.next
            slow = slow.next

        return fast


if __name__ == "__main__":
    print(Solution().loopDetection(LinkedList([1, 2, 3, 4, 5, 3])))




