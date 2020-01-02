"""
A binary search tree was created by traversing through an array from left to right and inserting each element.
Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

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


def bst_sequences(tree: TreeNode):
    return bst_sequences_partial([], [tree])


def bst_sequences_partial(partial, subtrees):
    if not len(subtrees):
        return [partial]
    sequences = []

    for index, subtree in enumerate(subtrees):
        next_partial = partial + [subtree.data]
        next_subtrees = subtrees[:index] + subtrees[index + 1:]
        if subtree.left:
            next_subtrees.append(subtree.left)
        if subtree.right:
            next_subtrees.append(subtree.right)

        sequences += bst_sequences_partial(next_partial, next_subtrees)
    return sequences


if __name__ == "__main__":
    print(bst_sequences(
        TreeNode(7, TreeNode(4,
                             TreeNode(5),
                             TreeNode(6)
                             ), TreeNode(9)
                 )
    ))
