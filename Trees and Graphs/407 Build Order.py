"""
You are given a list of projects and a list of dependencies
(which is a list of pairs of projects, where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

Solution:
1. Use depth-first search (DFS) to find the build path
2. In DFS, when we get to the end of a path and can't go any further, we know that those terminating
nodes can be the last projects to be built. No projects depend on them.
3. Add these projects to end of list or add visiting node to front of list
"""
__author__ = 'abhireddy96'


class GraphNode(object):

    def __init__(self, key):
        self.id = key
        self.adj = dict()  # key: vertex, val: weight
        self.state = 'UNVISITED'

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.adj])

    def add_edge(self, v, weight=0):
        self.adj[v] = weight

    def get_edges(self):
        return self.adj.keys()

    def get_id(self):
        return self.id

    def get_weight(self, x):
        return self.adj[x]

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


class Graph(object):

    def __init__(self, digraph=False):
        self.vertices = dict()  # key: id, val: vertex
        self.v = 0
        self.digraph = digraph

    def __contains__(self, v):
        return v in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, key):
        self.v += 1
        self.vertices[key] = GraphNode(key)

    def get_vertex(self, v):
        if v in self.vertices:
            return self.vertices[v]
        else:
            return None

    def add_edge(self, frm, to):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)
        self.vertices[frm].add_edge(self.vertices[to])
        if not self.digraph:
            self.vertices[to].add_edge(self.vertices[frm])

    def get_vertices(self):
        return self.vertices.keys()

    def reset_states(self):
        for v in iter(self):
            v.set_state('UNVISITED')


def buildGraph(projects, dependencies):
    graph = Graph(True)
    # Create each project as vertex
    for proj in projects:
        graph.add_vertex(proj)
    # Add dependencies as edges
    for to, frm in dependencies:
        graph.add_edge(frm, to)
    return graph


def dfs(res, vertex):
    # Avoid infinite looping on same vertex
    if vertex.get_state() == 'VISITING':
        return False

    # If Visiting vertex for first time
    if vertex.get_state() == 'UNVISITED':
        vertex.set_state('VISITING')
        # Traverse adjacent vertices
        for adj in vertex.get_edges():
            if not dfs(res, adj):
                return False
        # Mark Vertex as Visited
        vertex.set_state('VISITED')
        # Add vertex this vertex into begining as this needs to be visited first in order to visit other vertices
        res.insert(0, vertex.get_id())
    return True


def buildOrder(g):
    res = []
    # Iterate over each vertex of graph
    for v in iter(g):
        # Check if traversal is possible
        if not dfs(res, v):
            return None
    # Return resultant order of vertices
    return res


if __name__ == "__main__":
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [("d", "a"), ("b", "f"), ("d", "b"), ("a", "f"), ("c", "d")]
    graph = buildGraph(projects, dependencies)
    print(buildOrder(graph))
