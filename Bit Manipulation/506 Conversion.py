"""
Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
EXAMPLE
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2

Solution:
1. Each 1 in the XOR represents a bit that is different between A and B.
2. To check the number of bits that are different between A and B, count the number of bits in A^B(XOR) that are l.
3. Operation x = x & (x - 1) will clear the least significant bit in x.
"""
__author__ = 'abhireddy96'


class Solution:
    def conversion(self, a, b):
        x = a ^ b
        cnt = 0
        while x != 0:
            cnt += 1
            x &= x - 1
        return cnt


if __name__ == "__main__":
    print(Solution().conversion(329, 427))
