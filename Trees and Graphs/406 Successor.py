"""
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.
You may assume that each node has a link to its parent.

Solution:
1. In-order traversal traverses the left subtree, then the current node, then the right subtree
2. If node doesn't have a right subtree, we are done traversing subtree. Pick up where we left off with node's parent
3. In such case, traverse upwards until we find a node that we have not fully traversed.
"""
__author__ = 'abhireddy96'


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def successor(node: TreeNode):
    if not node:
        return None

    # If right child
    child = node.right
    if child:
        # Loop right subtree till last left node
        while child.left:
            child = child.left

    # return leftmost node of right subtree
    if child:
        return child

    # return parent of node
    if node.parent and node.parent.data > node.data:
        return node.parent

    return None


if __name__ == "__main__":
    print(
        successor(
            TreeNode(22,
                     TreeNode(11), TreeNode(33,
                                            TreeNode(28)
                                            )
                     )
        ).data
    )
