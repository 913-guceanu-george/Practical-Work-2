"""
    This is the second practical work fro the Graph Algo.
"""
from Graphs.exceptions import *
from copy import deepcopy
from queue import Queue
from heapq import *


class DirectedGraph:

    """
        The DirectedGraph class allows us to build a graph
    """

    def __init__(self):
        """
            Our graph is defined by its outbound neighbours and its inbound neighbours, so that's really all we need.
        """
        self.__outNeighbours = dict()
        self.__inNeighbours = dict()

    def addVertex(self, vertex):
        """
            Adds a vertex in the graph, unless it already exists.
        Args:
            vertex (int): The vertex we want to add

        Raises:
            VertexError: Raised in case of an impossible addition.
        """
        if vertex not in self.__outNeighbours.keys():
            self.__outNeighbours[vertex] = list()
            self.__inNeighbours[vertex] = list()
            return
        raise VertexError("Vertex already in graph")

    def addEdge(self, x, y):
        """
        Args:
            x (int): First vertex
            y (int): Second vertex

        Raises:
            EdgeError: If the edge is already in the graph, the it is raised.
        """
        if y not in self.__outNeighbours[x] and x not in self.__inNeighbours[y]:
            self.__outNeighbours[x].append(y)
            self.__inNeighbours[y].append(x)
            return
        raise EdgeError("Edge already exists!")

    def parseVertices(self):
        """
        Returns:
            list: A list containing all the vertices. 
        """
        return [x for x in self.__outNeighbours.keys()]

    def outbound(self, x):
        """
        Args:
            x (int): Given vertex

        Returns:
            list: A list with all its outbound neighbours.
        """
        return deepcopy(self.__outNeighbours[x])

    def inbound(self, x):
        """
        Args:
            x (int): The given vertex

        Returns:
            list: A list containing all the inbound neighbours.
        """
        return deepcopy(self.__inNeighbours[x])

    def isEdge(self, x, y):
        """
        Args:
            x (int): First vertex
            y (int): Second vertex.

        Returns:
            bool: True if the edge exists, False otherwise.
        """
        return y in self.__outNeighbours[x]


class Graph:

    # self.out_neighbors = dict from vertex to list of neighbors
    def __init__(self, vertices=[], edges=[]):
        self.out_neighbors = {}
        self.in_neighbors = {}
        for vertex in vertices:
            self.add_vertex(vertex)
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def add_vertex(self, vertex):
        if vertex not in self.out_neighbors.keys():
            self.out_neighbors[vertex] = []
            self.in_neighbors[vertex] = []
        else:
            raise ValueError("Vertex already in the graph!")

    def add_edge(self, x, y):
        if x not in self.out_neighbors.keys():
            raise ValueError(f"{x} vertex is not in the graph")
        if y not in self.out_neighbors.keys():
            raise ValueError(f"{y} vertex is not in the graph")
        if y in self.out_neighbors[x]:
            raise ValueError(f"{x}, {y} edge is already in the graph")
        self.out_neighbors[x].append(y)
        self.in_neighbors[y].append(x)

    def parse_vertices(self):
        return [x for x in self.out_neighbors.keys()]

    def outbound(self, x):
        return deepcopy(self.out_neighbors[x])

    def inbound(self, x):
        return deepcopy(self.in_neighbors[x])
        l = []
        for y in self.out_neighbors.keys():
            if x in self.out_neighbors[y]:
                l.append(y)
        return l

    def is_edge(self, x, y):
        return y in self.out_neighbors[x]


def trace(parent, x, y):
    """
        Checks the inbound neighbours of the current vertex (parent) and then if it can build a path from x to y.
    Args:
        parent (int): _description_
        x (int): _description_
        y (int): _description_

    Returns:
        list: path from x to y
    """
    path = [y]
    i = y
    while i != x:
        path.append(parent[i])
        i = parent[i]
    #  path.reverse() - modify this if reversed
    return path


def bfs(g, y, x):
    checked = []
    inbound = []
    for i in range(len(g.parseVertices()) + 1):
        checked.append(False)
        inbound.append(-1)
    queue = [y]
    while len(queue) > 0:
        print(queue)
        current = queue[0]
        queue.pop(0)
        if current == x:
            return trace(inbound, y, x)
        checked[current] = True
        for neighbour in g.inbound(current):
            if not checked[neighbour] and neighbour not in queue:
                inbound[neighbour] = current
                queue.append(neighbour)


def build_graph1():
    g = DirectedGraph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(5)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 2)
    g.addEdge(5, 4)
    return g


def create_graph_and_cost():
    g = Graph(range(10))
    cost = {
        (0, 1): 3,
        (0, 2): 6,
        (1, 2): 3,
        (0, 3): 3,
        (3, 2): 2,
        (2, 4): 10,
    }
    for edge in cost.keys():
        g.add_edge(edge[0], edge[1])
    return g, cost


def min_cost_path_dijkstra(g, cost, s, t):
    '''Finds the minimum cost path from s to t
    in the graph g. Returns a tuple containing the path as a list of vertices starting
    with s and ending with t, and the corresponding cost. Returns (None,None) if no path exists.
    '''
    dist, prev = dijkstra(g, cost, s, t)

    if t not in dist.keys():
        return None

    path = []
    y = t
    while y != s:
        path.append(y)
        y = prev[y]
    path.append(s)
    path.reverse()
    return path, dist[t]


def dijkstra(g, cost, s, t=None):
    dist = dict()
    prev = dict()
    dist[s] = 0
    q = list()
    heappush(q, (dist[s], s))

    while q:
        print(f"q={q}")
        distance, vertex = heappop(q)
        print(f"distance={distance}, vertex={vertex}")
        if vertex == t:
            break
        if distance == dist[vertex]:
            for neighbor in g.outbound(vertex):
                if neighbor not in dist or dist[neighbor] > dist[vertex] + cost[(vertex, neighbor)]:
                    dist[neighbor] = dist[vertex] + cost[(vertex, neighbor)]
                    prev[neighbor] = vertex
                    heappush(q, (dist[neighbor], neighbor))
        print(f"dist={dist}")
        print(f"prev={prev}")
    return dist, prev


def test_dijkstra():
    g, cost = create_graph_and_cost()
    print(min_cost_path_dijkstra(g, cost, 0, 0))


test_dijkstra()


# g = build_graph1()
# print(g.parseVertices())
# print(bfs(g, 4, 1))
