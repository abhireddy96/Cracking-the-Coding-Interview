"""
Tl and T2 are two very large binary trees, with Tl much bigger than T2. Determine if T2 is a subtree of Tl.
A tree T2 is a subtree of T1 if there exists a node n in Tl such that the subtree of n is identical to T2 .
That is, if you cut off the tree at node n, the two trees would be identical.

Solution:
If each node has a link to its parent, we could trace node1 and node2's paths up until they intersect.
"""
__author__ = 'abhireddy96'


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + ':L ' + "V:" + str(self.data) + " R:" + str(self.right) + ')'


def isSubtree(bt1, bt2):
    for node in treeGenerator(bt1):
        if equivalentTrees(node, bt2):
            return True
    return False


def equivalentTrees(bt1, bt2):
    if not bt1:
        return not bt2
    if not bt2:
        return False
    if bt1.data != bt2.data:
        return False
    return equivalentTrees(bt1.left, bt2.left) and \
           equivalentTrees(bt1.right, bt2.right)


def treeGenerator(node):
    if not node:
        return
    yield node
    for child in treeGenerator(node.left):
        yield child
    for child in treeGenerator(node.right):
        yield child


if __name__ == "__main__":
    tree1 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8, TreeNode(7, TreeNode(9)), TreeNode(1)))
    tree2 = TreeNode(8, TreeNode(7), TreeNode(1))
    print(isSubtree(tree1, tree2))
    tree3 = TreeNode(8, TreeNode(7, TreeNode(9)), TreeNode(1))
    print(isSubtree(tree1, tree3))
