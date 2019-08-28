"""
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase
that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations:"taco cat'; "atco cta'; etc.)

Solution:
1. Use a hash table to count how many times each character appears.
2. Iterate through the hash table and ensure that no more than one character has an odd count.
"""
__author__ = 'abhireddy96'
from collections import Counter


class Solution:
    def palindromePermutation(self, phrase: str):
        # Initialize Counter
        counter = Counter()
        # Keep tack of odd char counts
        oddCount = 0

        # Iterate over lower character string of phrase
        for c in phrase.lower():
            # Check if it is alphabet
            if c.isalpha():
                # Add char to counter
                counter[c] += 1
                # Count is odd
                if (counter[c] % 2) != 0:
                    oddCount += 1
                else:
                    oddCount -= 1
        # odd char count should be less or equal to 1
        return oddCount <= 1


if __name__ == "__main__":
    print(Solution().palindromePermutation('Tact Coa'))
    print(Solution().palindromePermutation('no x in nixon@'))

