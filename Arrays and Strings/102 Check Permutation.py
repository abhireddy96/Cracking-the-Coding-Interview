"""
Given two strings, write a method to decide if one is a permutation of the other.

Solution:
Iterate through string, counting how many times each character appears and compare the two arrays.
"""
__author__ = 'abhireddy96'
from collections import Counter


class Solution:
    def checkPermutation(self, str1: str, str2: str):

        # Check if two string are of same length
        if len(str1) != len(str2):
            return False

        # Initialize Counter DS
        counter = Counter()

        # Iterate over str1, create counter of chars
        for c in str1:
            counter[c] += 1

        # Iterate over str2, subtract char count from counter
        for c in str2:
            # Mismatch in char count
            if counter[c] == 0:
                return False
            counter[c] -= 1

        return True


if __name__ == "__main__":
    print(Solution().checkPermutation('abcd', 'adcb'))

