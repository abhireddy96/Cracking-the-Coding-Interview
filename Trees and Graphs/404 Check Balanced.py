"""
Implement a function to check if a binary tree is balanced. A balanced tree is defined to be a tree such that the
heights of the two subtrees of any node never differ by more than one.

Solution:
1. Check the height of each subtree as we recurse down from the root.
2. On each node, we recursively get the heights of the left and right subtrees
3. If the subtree is balanced, return true with depth
"""
__author__ = 'abhireddy96'


class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def isBalanced(rootNode):
    if not rootNode:
        return [True, 0]

    # Traverse over left sub tree
    left_balanced, left_depth = isBalanced(rootNode.left)
    if not left_balanced:
        return [False, None]

    # Traverse over right sub tree
    right_balanced, right_depth = isBalanced(rootNode.right)
    # Check if left n right subtree depth diff is more than 1 level
    if (not right_balanced) or (abs(left_depth - right_depth) > 1):
        return [False, None]

    # Find MAX Depth if both left n right subtrees are balanced
    depth = max(left_depth, right_depth) + 1

    return [True, depth]


if __name__ == "__main__":
    print(isBalanced(TreeNode(
        TreeNode(
            TreeNode()
        ),
        TreeNode(
            TreeNode(
                TreeNode()
            ),
            TreeNode()
        )
    )
    )
    )
