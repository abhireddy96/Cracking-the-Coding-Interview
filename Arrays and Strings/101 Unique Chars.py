"""
Implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures?

Solution:
1. Create an array of boolean values, where the flag at index i indicates whether character i in the alphabet is in string.
2. The second time you see this character, immediately return false.
"""
__author__ = 'abhireddy96'


class Solution:
    def isUnique(self, s: str) -> bool:
        # Assuming character set is ASCII (128 characters)
        if len(s) > 128:
            return False

        # Initialize list with False
        char_set = [False for _ in range(128)]

        for char in s:
            # ASCII value of Char
            val = ord(char)
            if char_set[val]:
                # Char already found in string
                return False
            char_set[val] = True

        return True


if __name__ == "__main__":
    print(Solution().isUnique('abcd'))
    print(Solution().isUnique('aabd'))




