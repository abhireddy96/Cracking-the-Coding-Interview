"""
Find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.

Solution:
If each node has a link to its parent, we could trace node1 and node2's paths up until they intersect.
"""
__author__ = 'abhireddy96'


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None
        # Make this node as parent of left n right child nodes
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __str__(self):
        return '(' + str(self.left) + ':L ' + "V:" + str(self.data) + " R:" + str(self.right) + ')'


def firstCommonAncestor(node1: TreeNode, node2: TreeNode):
    ancestors1, ancestors2 = {}, {}
    # Iterate upwards
    while node1 or node2:
        if node1:
            # Check if node1 is already a ancestor of node2
            if node1 in ancestors2:
                return node1
            # Add this as ancestor of node 1
            ancestors1[node1] = True
            node1 = node1.parent
        if node2:
            # Check if node2 is already a ancestor of node1
            if node2 in ancestors1:
                return node2
            # Add this as ancestor of node 2
            ancestors2[node2] = True
            node2 = node2.parent
    return None


if __name__ == "__main__":
    node1 = TreeNode(11, TreeNode(55), TreeNode(77, TreeNode(44)))
    node2 = TreeNode(22, TreeNode(99))
    print(firstCommonAncestor(node1, node2))
    node3 = TreeNode(33, node1, TreeNode(88, TreeNode(123, None, node2)))
    node4 = TreeNode(44, node3, TreeNode(66))
    print(firstCommonAncestor(node1, node2))
