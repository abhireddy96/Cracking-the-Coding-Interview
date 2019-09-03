"""
You are given two 32-bit numbers N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at bit i.
(You can assume that the bits j through i have enough space to fit all of M.)

EXAMPLE
Input:  N = 10000000000 , M = 10011 , i = 2, j = 6
Output: N = 10001001100

Solution:
1. Clear the bits j through i in N
2. Shift M so that it lines up with bits j through i
3. Merge M and N.
(Trick to Clear Bits by masking - Mask will have all 1's, except for 0's in the bits j through i.
Create this mask by creating the left half of the mask first, and then the right half.)
"""
__author__ = 'abhireddy96'


class Solution:
    def insertion(self, n, m, i, j):

        # 1's before position j
        left = 1 << (j + 1)
        print('left = '+bin(left))

        # 1's after position i
        right = (1 << i)-1
        print('right = ' + bin(right))

        # All 1's, except for as between i and j.
        mask = left | right
        print('mask = ' + bin(mask))

        # Clear bits j through i
        clearedN = n & mask
        print('clearedN = ' + bin(clearedN))

        # Move m into correct position
        shiftedM = m << i
        print('shiftedM = ' + bin(shiftedM))

        # Put M in N
        return clearedN | shiftedM


if __name__ == "__main__":
    print(bin(Solution().insertion(0b11111111, 0b10, 2, 5)))
    print(bin(Solution().insertion(0b00000000, 0b1010, 4, 7)))




