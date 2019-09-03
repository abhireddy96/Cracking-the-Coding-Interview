"""
Given a real number between 8 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation.
If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR:'

Solution:
1. Compare number to . 5, then. 25, and so on
"""
__author__ = 'abhireddy96'


class Solution:
        def binaryToString(self, num):

            if num <= 0 or num >= 1:
                return "ERROR"

            res = '.'
            frac = 0.5

            while num > 0:
                # Setting a limit on length: 32 characters
                if len(res) >= 32:
                    return res

                # If num is greater than frac
                if num >= frac:
                    # Append 1 to result and subtract frac from num
                    res += '1'
                    num -= frac
                else:
                    # Append 0 to result
                    res += '0'
                # Take half from frac after each iteration
                frac /= 2.0
            return res


if __name__ == "__main__":
    print(Solution().binaryToString(0.72))




