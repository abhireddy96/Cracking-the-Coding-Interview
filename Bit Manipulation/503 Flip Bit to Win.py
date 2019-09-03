"""
You have an integer and you can flip exactly one bit from a 0 to a 1.
Find the length of the longest sequence of 1 s you could create.

EXAMPLE
Input: 1775 (or: 11011101111)
Output: 8

Solution:
1. Compare each 1 s sequence to the immediately preceding 1 s sequence.
2. Track the current 1 s sequence length and the previous 1 s sequence length.
3. If the next bit is a 1, previous Length should be set to currentLength.
4. If the next bit is a 0, then we can't merge these sequences together. Set previous Length to 0.
"""
__author__ = 'abhireddy96'


class Solution:
    def flipBitToWin(self, n):

        n = bin(n)
        currentLength = 0
        previousLength = 0
        maxLength = 1  # can always have a sequence of at least one 1

        for i in range(2, len(n) + 1):
            # Increment prev length until bit is 1
            if i < len(n) and n[i] == '1':
                previousLength += 1
            else:
                # Update all lengths
                if currentLength + previousLength + 1 > maxLength:
                    maxLength = currentLength + previousLength + 1
                currentLength = previousLength
                previousLength = 0
        return maxLength


if __name__ == "__main__":
    print(Solution().flipBitToWin(114409))




