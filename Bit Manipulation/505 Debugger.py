"""
Explain what the following code does: «n & (n-1)) == 0).

Solution:
A&B means that A and B never have a 1 bit in the same place. So if n & (n -1)==0, then n and n -1 never share a 1.
"""
__author__ = 'abhireddy96'


class Solution:
    def isPowerOfTwoOrZero(self, n):
        return (n & (n - 1)) == 0


if __name__ == "__main__":
    print(Solution().isPowerOfTwoOrZero(3))
    print(Solution().isPowerOfTwoOrZero(2))
