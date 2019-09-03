"""
Given a positive integer, print the next smallest and the next largest number that have the
same number of 1 bits in their binary representation.

Solution:
1. If c0 is the number of trailing zeros, c1 is the size of the one block immediately following, and p=c0+c1
To find largest number:
- Set the pth bit to 1.
- Set all bits following p to 0.
(A quick and dirty way to perform above steps is to set the trailing zeros to 1 (giving us p trailing ones), and
then add 1. Adding one will flip all trailing ones, so we wind up with a 1 at bit p followed by p zeros.)
- Set bits 0 through c1-2 to 1. This will be c1-1 total bits.

2. If c1 is the number of trailing ones, c0 is the size of the zero block immediately following, and p=c0+c1
To find smallest number:
- Set the pth bit to 0.
- Set all bits following p to 1.
- Set bits 0 through c0-1 to 0.
"""
__author__ = 'abhireddy96'


class Solution:
    def nextNumber(self, num):

        return [self.findPrev(num), self.findNext(num)]

    def findNext(self, n):
        c = n
        c0 = 0
        c1 = 0
        while (c & 1) == 0 and c != 0:
            c0 += 1
            c >>= 1
        while (c & 1) == 1:
            c1 += 1
            c >>= 1
        if c0 + c1 == 53 or c0 + c1 == 0:
            return None
        return n + (1 << c0) + (1 << (c1 - 1)) - 1

    def findPrev(self, n):
        c = n
        c0 = 0
        c1 = 0
        while (c & 1) == 1:
            c1 += 1
            c >>= 1
        if c == 0:
            return None
        while (c & 1) == 0 and c != 0:
            c0 += 1
            c >>= 1
        return n - ((1 << c1) - 1) - 1 - ((1 << (c0 - 1)) - 1)


if __name__ == "__main__":
    print(Solution().nextNumber(15))
