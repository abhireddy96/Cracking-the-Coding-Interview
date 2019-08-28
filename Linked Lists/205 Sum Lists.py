"""
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1 's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2) .That is,617 + 295.
Output: 2 - > 1 - > 9. That is, 912.

Solution:
Basic School math addition approach of sum and carry.
"""
__author__ = 'abhireddy96'
from LinkedList import LinkedList


class Solution:
    def sumLists(self, ll_a, ll_b):
        n1, n2 = ll_a.head, ll_b.head
        # Resultant list
        res = LinkedList()
        carry = 0

        # Loop till longest list
        while n1 or n2:
            result = carry
            # Add values at corresponding nodes
            if n1:
                result += n1.value
                n1 = n1.next
            if n2:
                result += n2.value
                n2 = n2.next
            # If value is greater than 9
            res.add(result % 10)  # Add last digit
            carry = result // 10  # remaining will be carry

        # If carry is remaining
        if carry:
            res.add(carry)

        return res


if __name__ == "__main__":
    ll_a = LinkedList()
    ll_a.generate(4, 0, 9)
    ll_b = LinkedList()
    ll_b.generate(3, 0, 9)
    print(ll_a)
    print(ll_b)
    print(Solution().sumLists(ll_a, ll_b))




