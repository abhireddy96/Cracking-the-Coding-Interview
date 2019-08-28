"""
Write a method to replace all spaces in a string with %20: You may assume that the string has sufficient space at the
end to hold the additional characters, and that you are given the "true" length of the string.
(Note: if implementing in Java, please use a character array so that you can perform this operation in place.)
EXAMPLE
Input: "Mr John Smith JJ, 13
Output: "Mr%2eJohn%2eSmith"

Solution:
1. First scan, we count the number of spaces.
2. By tripling this number, we can compute how many extra characters we will have in the final string.
3. In the second pass, which is done in reverse order, we actually edit the string.
4. When we see a space, we replace it with %20. If there is no space, then we copy the original character.
"""
__author__ = 'abhireddy96'


class Solution:
    def urlify(self, s: str, length: int):
        s = list(s)
        # Pointer
        sLen = len(s)

        # Iterate over string in reverse order
        for i in range(length-1, -1, -1):
            if s[i] == ' ':
                # Replace spaces
                s[sLen - 3:sLen] = '%20'
                sLen -= 3
            else:
                # Move characters
                s[sLen - 1] = s[i]
                sLen -= 1
            print(''.join(s))
        return ''.join(s)


if __name__ == "__main__":
    print(Solution().urlify('much ado about nothing      ', 22))

