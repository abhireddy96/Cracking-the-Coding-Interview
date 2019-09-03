"""
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

Solution:
1. Insert into the tree the middle element of the array.
2. Insert (into the left subtree) the left subarray elements.
3. Insert (into the right subtree) the right subarray elements.
"""
__author__ = 'abhireddy96'


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + ':L ' + "V:" + str(self.data) + " R:" + str(self.right) + ')'


def minimalHeightBST(arr):
    if len(arr) == 0:
        return None
    # Find middle
    middle = len(arr) // 2
    # Recurse over left array
    left = minimalHeightBST(arr[:middle])
    # Recurse over right array
    right = minimalHeightBST(arr[(middle + 1):])
    # create node with middle as parent
    return BSTNode(arr[middle], left, right)


if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(minimalHeightBST([1, 2, 3, 4, 5, 6, 7, 8, 9]))
