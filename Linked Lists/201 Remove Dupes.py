"""
Write code to remove duplicates from an unsorted linked list.

Solution:
1. Simply iterate through the linked list, adding each element to a Set.
2. When we discover a duplicate element, we remove the element from list and continue iterating.
3. We can do this all in one pass since we are using a linked list.
"""
__author__ = 'abhireddy96'
from LinkedList import LinkedList


class Solution:
    def removeDupes(self, ll: LinkedList):

        # If list is empty
        if ll.head is None:
            return

        # Assign head to current
        current = ll.head
        # Set of distinct nodes
        seen = set([current.value])

        # Iterate over list
        while current.next:
            # If node is already present in set
            if current.next.value in seen:
                # Unlink node
                current.next = current.next.next
            else:
                # Add node n proceed to next
                seen.add(current.next.value)
                current = current.next

        return ll


if __name__ == "__main__":
    ll = LinkedList()
    ll.generate(20, 0, 9)
    print(ll)
    Solution().removeDupes(ll)
    print(ll)




