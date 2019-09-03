"""
Swap odd and even bits in an integer with as few instructions as possible
(e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

Solution:
1. Mask all odd bits with 10101010 in binary (which is 0xAA), shift them right by 1 to put them in the even spots.
2. Mask all even bits with 01010101 in binary (which is 0x55), shift them left by 1 to put them in the odd spots.
3. Finally perform OR operation between both
"""
__author__ = 'abhireddy96'


class Solution:
    def swapOddEvenBits(self, n):
        evenMask = 0x5555555555555555
        oddMask = 0xAAAAAAAAAAAAAAAA
        return (n & oddMask) >> 1 | (n & evenMask) << 1


if __name__ == "__main__":
    print(Solution().swapOddEvenBits(1023))
    print(Solution().swapOddEvenBits(21))
