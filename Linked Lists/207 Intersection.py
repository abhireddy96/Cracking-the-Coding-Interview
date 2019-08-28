"""
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list
is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

Solution:
1. Run through each linked list to get the lengths and the tails.
2. Compare the tails. If they are different (by reference, not by value), return immediately. There is no intersection.
3. Set two pointers to the start of each linked list.
4. On the longer linked list, advance its pointer by the difference in lengths.
5. Traverse on each linked list until the pointers are the same.
"""
__author__ = 'abhireddy96'
from LinkedList import LinkedList


class Solution:
    def intersection(self, list1, list2):

        # Compare the tails
        # If they are different, There is no intersection.
        if list1.tail is not list2.tail:
            return False

        shorter = list1 if len(list1) < len(list2) else list2
        longer = list2 if len(list1) < len(list2) else list1

        # Find length diff b/w shorter n longer list
        diff = len(longer) - len(shorter)

        shorter_node, longer_node = shorter.head, longer.head

        # Iterate longer list
        for i in range(diff):
            longer_node = longer_node.next

        # If nodes are not equal, Iterate both the lists
        # Colliding point will be intersecting node
        while shorter_node is not longer_node:
            shorter_node = shorter_node.next
            longer_node = longer_node.next

        return longer_node


if __name__ == "__main__":
    print(Solution().intersection(LinkedList([3, 1, 5, 9, 7, 2, 1]), LinkedList([4, 6, 7, 2, 1])))




