from exceptions import *
from random import randrange
from copy import deepcopy


class UndirectedGraph:
    def __init__(self, n=0, m=0):
        self.__vertices = set()
        self.__neighbours = dict()
        self.__cost = dict()
        for i in range(n):
            self.addVertex(i)
        for j in range(m):
            vertex1 = randrange(n)
            vertex2 = randrange(n)
            while self.isEdge(vertex1, vertex2):
                vertex1 = randrange(n)
                vertex2 = randrange(n)
            self.addEdge(vertex1, vertex2, randrange(10000))

    def verticesIterator(self):
        """
        Returns an iterator to the set of vertices.
        """
        for vertex in self.__vertices:
            yield vertex

    def neighboursIterator(self, vertex):
        """
        Returns an iterator to the set of (outbound) neighbours of a vertex.
        """
        if not self.isVertex(vertex):
            raise VertexError("Invalid vertex.")
        for neighbour in self.__neighbours[vertex]:
            yield neighbour

    def edgesIterator(self):
        """
        Returns an iterator to the set of edges.
        """
        for key, value in self.__cost.items():
            yield key[0], key[1], value

    def isVertex(self, vertex):
        """
        Returns True if vertex belongs to the graph.
        """
        return vertex in self.__vertices

    def isEdge(self, vertex1, vertex2):
        """
        Returns True if the edge from vertex1 to vertex2 belongs to the graph.
        """
        if vertex1 > vertex2:
            vertex1, vertex2 = vertex2, vertex1
        return vertex1 in self.__neighbours and vertex2 in self.__neighbours[vertex1]

    def countVertices(self):
        """
        Returns the number of vertices in the graph.
        """
        return len(self.__vertices)

    def countEdges(self):
        """
        Returns the number of edges in the graph.
        """
        return len(self.__cost)

    def degree(self, vertex):
        """
        Returns the number of edges with the start point vertex.
        """
        if vertex not in self.__neighbours:
            raise VertexError("The specified vertex does not exist.")
        return len(self.__neighbours[vertex])

    def getEdgeCost(self, vertex1, vertex2):
        """
        Returns the cost of an edge if it exists.
        """
        if vertex1 > vertex2:
            vertex1, vertex2 = vertex2, vertex1
        if (vertex1, vertex2) not in self.__cost:
            raise EdgeError("The specified edge does not exist.")
        return self.__cost[(vertex1, vertex2)]

    def setEdgeCost(self, vertex1, vertex2, new__cost):
        """
        Sets the cost of an edge in the graph if it exists.
        """
        if vertex1 > vertex2:
            vertex1, vertex2 = vertex2, vertex1
        if (vertex1, vertex2) not in self.__cost:
            raise EdgeError("The specified edge does not exist.")
        self.__cost[(vertex1, vertex2)] = new__cost

    def addVertex(self, vertex):
        """
        Adds a vertex to the graph.
        """
        if self.isVertex(vertex):
            raise VertexError("Cannot add a vertex which already exists.")
        self.__vertices.add(vertex)
        self.__neighbours[vertex] = set()

    def addEdge(self, vertex1, vertex2, edge__cost=0):
        """
        Adds an edge to the graph.
        """
        if vertex1 > vertex2:
            vertex1, vertex2 = vertex2, vertex1
        if self.isEdge(vertex1, vertex2):
            raise EdgeError("The specified edge already exists")
        if not self.isVertex(vertex1) or not self.isVertex(vertex2):
            raise EdgeError("The vertices on the edge do not exist.")
        self.__neighbours[vertex1].add(vertex2)
        self.__neighbours[vertex2].add(vertex1)
        self.__cost[(vertex1, vertex2)] = edge__cost

    def removeEdge(self, vertex1, vertex2):
        """
        Removes an edge from the graph.
        """
        if vertex1 > vertex2:
            vertex1, vertex2 = vertex2, vertex1
        if not self.isEdge(vertex1, vertex2):
            raise EdgeError("The specified edge does not exist.")
        del self.__cost[(vertex1, vertex2)]
        self.__neighbours[vertex1].remove(vertex2)
        self.__neighbours[vertex2].remove(vertex1)

    def removeVertex(self, vertex):
        """
        Removes a vertex from the graph.
        """
        if not self.isVertex(vertex):
            raise VertexError("Cannot remove a vertex which doesn't exist.")
        to_remove = []
        for node in self.__neighbours[vertex]:
            to_remove.append(node)
        for node in to_remove:
            self.removeEdge(vertex, node)
        del self.__neighbours[vertex]
        self.__vertices.remove(vertex)

    def copy(self):
        """
        Returns a deepcopy of the graph.
        """
        return deepcopy(self)
