"""
Implement an algorithm to find the kth to last element of a singly linked list.

Solution:
1. Use two pointers, p1 and p2. P
2. Place them k nodes apart in the linked list by putting p2 at the beginning and moving p1 k nodes into the list.
3. Move them at the same pace, p1 will hit the end of the linked list after LENGTH - k steps.
4. At that point, p2 will be LENGTH - k nodes into the list, or k nodes from the end.
"""
__author__ = 'abhireddy96'
from LinkedList import LinkedList


class Solution:
    def kTHtoLast(self, ll, k):
        p1 = p2 = ll.head

        # Iterate p1 to Kth node from begining
        for i in range(k):
            if p1 is None:
                return None
            p1 = p1.next

        # Iterate p1 till EOL n also Iterate p2 simultaneously
        while p1:
            p2 = p2.next
            p1 = p1.next

        # p1 will hit the end of the linked list after LENGTH - k steps.
        # At that point, p2 will be LENGTH - k nodes into the list, or k nodes from the end.
        return p2.value


if __name__ == "__main__":
    ll = LinkedList()
    ll.generate(20, 0, 9)
    print(ll)
    print(Solution().kTHtoLast(ll, 4))




