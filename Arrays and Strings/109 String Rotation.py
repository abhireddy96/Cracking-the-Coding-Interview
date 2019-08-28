"""
Assume you have a method i5Substring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
(e.g., Uwaterbottleuis a rotation ofuerbottlewatU ).

Solution:
Split s1 into x and y such that xy = s1 and yx = s2.
Regardless of where the division between x and y is, we can see that yx will always bea substring of xyxy.
s2 will always be a substring of s1s1.
"""
__author__ = 'abhireddy96'


class Solution:
    def stringRotation(self, s1: str, s2: str):
        if len(s1) == len(s2):
            # s2 will always be a substring of s1s1
            return (s1*2).find(s2) != 1
        return False


if __name__ == "__main__":
    print(Solution().stringRotation('waterbottle', 'erbottlewat'))




