"""
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

Solution:
1. Perform depth-first search or breadth-first search.
2. Start with one of the two nodes and, check if the other node is found.
3. Mark any node found in the course of the algorithm as "already visited" to avoid cycles and repetition of the nodes.
"""
__author__ = 'abhireddy96'


class Graph:

    def __init__(self):
        self.max_vertices = 6
        self.vertices = [0] * self.max_vertices
        self.count = 0

    def addNode(self, x):
        if self.count < self.max_vertices:
            self.vertices[self.count] = x
            self.count += 1
        else:
            print("Graph full")

    def getNodes(self):
        return self.vertices


class Node:

    def __init__(self, vertex, adjacentLength):
        self.adjacent = [0] * adjacentLength
        self.vertex = vertex
        self.adjacentCount = 0
        self.visited = False

    def addAdjacent(self, x):
        if self.adjacentCount < len(self.adjacent):
            self.adjacent[self.adjacentCount] = x
            self.adjacentCount += 1
        else:
            print("No more adjacent nodes can be added")

    def getAdjacent(self):
        return self.adjacent

    def getVertex(self):
        return self.vertex


class Queue:
    def __init__(self):
        self.array = []

    def put(self, item):
        self.array.append(item)

    def get(self):
        if not len(self.array):
            return None
        item = self.array[0]
        del self.array[0]
        return item

    def empty(self):
        return self.array == []


def createNewGraph():
    g = Graph()
    sizegraph = 6
    temp = [0] * sizegraph

    temp[0] = Node("a", 3)
    temp[1] = Node("b", 0)
    temp[2] = Node("c", 0)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 1)
    temp[5] = Node("f", 0)

    temp[0].addAdjacent(temp[1])
    temp[0].addAdjacent(temp[2])
    temp[0].addAdjacent(temp[3])
    temp[3].addAdjacent(temp[4])
    temp[4].addAdjacent(temp[5])

    for i in range(sizegraph):
        g.addNode(temp[i])
    return g


def createNewGraphWithLoop():
    g = Graph()
    sizegraph = 6
    temp = [0] * sizegraph

    temp[0] = Node("a", 1)
    temp[1] = Node("b", 1)
    temp[2] = Node("c", 1)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 2)
    temp[5] = Node("f", 0)

    temp[0].addAdjacent(temp[1])
    temp[1].addAdjacent(temp[2])
    temp[2].addAdjacent(temp[3])
    temp[3].addAdjacent(temp[4])
    temp[4].addAdjacent(temp[1])
    temp[4].addAdjacent(temp[5])

    for i in range(sizegraph):
        g.addNode(temp[i])
    return g


def breadthFirstSearch(start, end):
    # Check if same node
    if start == end:
        return True
    q = Queue()

    # Make start node as visited n add it into queue
    start.visited = True
    q.put(start)

    # Until queue is empty
    while not q.empty():
        # Dequeue
        r = q.get()
        # If node is present
        if r is not None:
            # Fetch adjacent nodes
            adjacent = r.getAdjacent()
            # Iterate over adjacent nodes
            for i in range(len(adjacent)):
                # If node is not visited before
                if not adjacent[i].visited:
                    # Check if it is equal to end node
                    if adjacent[i] == end:
                        return True
                    # Add this adjacent node into queue
                    # Mark it visited
                    else:
                        q.put(adjacent[i])
                    adjacent[i].visited = True
    return False


if __name__ == "__main__":
    g = createNewGraphWithLoop()
    n = g.getNodes()
    start = n[0]
    end = n[5]
    print("Start at:", start.getVertex(), "End at: ", end.getVertex())
    print(breadthFirstSearch(start, end))
