"""
Implement a function to check if a binary tree is a binary search tree.

Solution:
1. All left nodes must be less than or equal to the current node, which must be less than all the right nodes.
2. Branch left, the max gets updated.
3. Branch right, the min gets updated.
"""
__author__ = 'abhireddy96'


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def validateBST(root: TreeNode):
    return isBSTnode(root, -float('inf'), float('inf'))


def isBSTnode(node, left_min, right_max):
    if not node:
        return True

    # Check if left <= root <= right
    # Recurse over left node with updated max_right(current node value)
    # Recurse over right node with updated left_min(current node value)
    return left_min <= node.data <= right_max and \
           isBSTnode(node.left, left_min, node.data) and \
           isBSTnode(node.right, node.data, right_max)


if __name__ == "__main__":
    print(
        validateBST(
            TreeNode(5,
                     TreeNode(3, TreeNode(1), TreeNode(4)),
                     TreeNode(7, TreeNode(6), TreeNode(8, None, TreeNode(9))
                              )
                     )
        )
    )
