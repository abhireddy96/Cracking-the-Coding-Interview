"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Solution:
1. Iterate through the string counting the repeats.
2. At each iteration, check if current character is the same as the next character.
   If not, add its compressed version to the result.
"""
__author__ = 'abhireddy96'


class Solution:
    def stringCompression(self, s: str):
        compressed = list()
        counter = 0

        # Iterate over string
        for i in range(len(s)):
            # check if char is not same as previous char
            if i != 0 and s[i] != s[i - 1]:
                # Add char n it's count
                compressed.append(s[i - 1] + str(counter))
                counter = 0
            # Increment counter if not equal
            counter += 1

        # Add last repeated character
        compressed.append(s[-1] + str(counter))
        res = ''.join(compressed)

        # Returns original string if compressed string isn't smaller
        return s if len(s) <= len(res) else res


if __name__ == "__main__":
    print(Solution().stringCompression('aabcccccaaa'))
    print(Solution().stringCompression('abcdef'))




