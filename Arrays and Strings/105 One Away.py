"""
There are three types of edits that can be performed on strings: insert a character, remove a character,
or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -) true
pales, pale -) true
pale, bale -) true
pale, bae -) false

Solution:
Check all possible strings that are one edit away by
1. Testing the removal of each character (and comparing)
2. Testing the replacement of each character (and comparing)
3. Testing the insertion of each possible character (and comparing)
"""
__author__ = 'abhireddy96'


class Solution:
    def one_away(self, s1, s2):
        # Check if length of strings differ by zero or one character
        # If length of strings is same, then do replace operation
        if len(s1) == len(s2):
            return self.one_edit_replace(s1, s2)
        # If length of strings is diff, then do insert operation
        elif len(s1) + 1 == len(s2):
            return self.one_edit_insert(s1, s2)
        elif len(s1) - 1 == len(s2):
            return self.one_edit_insert(s2, s1)

        return False

    # Function to perform replace operation
    def one_edit_replace(self, s1, s2):
        edited = False
        for c1, c2 in zip(s1, s2):
            # Check if char at a index is same for both the strings
            if c1 != c2:
                # If already edited
                if edited:
                    return False
                edited = True
        return True

    # Function to perform insert operation
    def one_edit_insert(self, s1, s2):
        edited = False
        i = 0
        j = 0
        # Iterate over s1 and s2
        while i < len(s1) and j < len(s2):
            # If chars at pos i,j are diff
            if s1[i] != s2[j]:
                # If already edited
                if edited:
                    return False
                edited = True
                # Iterate to next char in string two
                j += 1
            else:
                # Iterate to next chars in strings
                i += 1
                j += 1
        return True


if __name__ == "__main__":
    print(Solution().one_away('pale', 'ple'))
