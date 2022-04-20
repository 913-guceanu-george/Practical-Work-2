from exceptions import *
from copy import deepcopy
from queue import Queue


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


g = build_graph1()
print(g.parseVertices())
print(bfs(g, 4, 1))
