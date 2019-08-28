"""
Implement a function to check if a linked list is a palindrome.

Solution:
1. Create two pointers, FastPointer and SlowPointer.
2. Move FastPointer at a rate of 2 steps and SlowPointer at a rate of 1 step.
3. Push the data from the slow runner onto a stack(first half of the elements onto a stack)
4. Iterate till fast runner hits the end of the list, now slow runner will have reached he middle of the linked list.
5. Iterate through the rest of the linked list. At each iteration, we compare the node to the top of the stack
"""
__author__ = 'abhireddy96'
from LinkedList import LinkedList


class Solution:
    def palindrome(self, ll):
        fast = slow = ll.head
        stack = []

        # Iterate through list with two pointers
        while fast and fast.next:
            # Push slow pointer value into stack
            stack.append(slow.value)
            # Iterate slow pointer by 1
            slow = slow.next
            # Iterate fast pointer by 2
            fast = fast.next.next

        # In case of odd length
        if fast:
            slow = slow.next

        # Fast pointer reached EOL
        # Slow pointer in middle of list

        # Iterate with slow pointer(Which currently points to middle of list)
        while slow:
            top = stack.pop()

            # Compare stack top with slow pointer value
            if top != slow.value:
                return False

            slow = slow.next

        return True


if __name__ == "__main__":
    print(Solution().palindrome(LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])))
    print(Solution().palindrome(LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])))




