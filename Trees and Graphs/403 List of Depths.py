"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
(e.g., if you have a tree with depth D, you 'll have D linked lists).

Solution:
1. Implement a simple modification of the breadth-first search.
2. Iterate through the root first, then level 2, then level 3, and so on.
3. With each level i , we will have already fully visited all nodes on level i - 1.
   Means that to get nodes are on level i, we can simply look at all children of the nodes of level i - l.
"""
__author__ = 'abhireddy96'


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.depth = None


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + ',' + str(self.next)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        if self.head:
            self.tail.next = ListNode(item)
            self.tail = self.tail.next
        else:
            self.head = self.tail = ListNode(item)

    def remove(self):
        if not self.head:
            return None
        item = self.head.data
        self.head = self.head.next
        return item


def listOfDepths(node: TreeNode):
    resList = list()
    queue = Queue()

    tail = None
    depth = -1
    node.depth = 0

    while node:
        # If current node is at level of depth
        if node.depth == depth:
            # Add current node to tail next N make current node as tail
            tail.next = ListNode(node.data)
            tail = tail.next
        else:
            # Assign current node depth
            depth = node.depth
            # Create ListNode from TreNode
            tail = ListNode(node.data)
            # Add this node to resultant list
            resList.append(tail)
        # Traverse over children of current node
        for child in [node.left, node.right]:
            if child:
                # Child depth will be +1 of parent or current node
                # Push into into queue
                child.depth = node.depth + 1
                queue.add(child)
        # Remove Node from queue and repeat process
        node = queue.remove()
    return resList


if __name__ == "__main__":
    node_h = TreeNode('H')
    node_g = TreeNode('G')
    node_f = TreeNode('F')
    node_e = TreeNode('E', node_g)
    node_d = TreeNode('D', node_h)
    node_c = TreeNode('C', None, node_f)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)
    for l in listOfDepths(node_a):
        print(l)
