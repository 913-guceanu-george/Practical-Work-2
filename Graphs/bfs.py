from directedGraph import *
from undirectedGraph import *
import queue


def connected_components(graph):
    met = set()
    ans = []
    for vertex in graph.verticesIterator():
        if vertex not in met:
            q = queue.Queue()
            q.put(vertex)
            met.add(vertex)
            ans.append([vertex])
            while not q.empty():
                node = q.get()
                for neighbour in graph.neighboursIterator(node):
                    if neighbour not in met:
                        met.add(neighbour)
                        q.put(neighbour)
                        ans[-1].append(neighbour)
    return ans


def strongly_connected_components(graph):
    met = set()
    order = []

    def dfs(x):
        met.add(x)
        for y in graph.neighboursIterator(x):
            if y not in met:
                dfs(y)
        order.append(x)

    for node in graph.verticesIterator():
        if node not in met:
            dfs(node)

    met2 = set()

    def dfs_t(x, sol):
        met2.add(x)
        sol.append(x)
        for y in graph.transposeIterator(x):
            if y not in met2:
                dfs_t(y, sol)

    ans = []
    for node in reversed(order):
        if node not in met2:
            ans.append([])
            dfs_t(node, ans[-1])
    return ans


ug = UndirectedGraph(5, 10)
for triple in ug.edgesIterator():
    print(triple[0], triple[1])

print(connected_components(ug))
print("\n\n")

g = DirectedGraph(7, 9)
for triple in g.edgesIterator():
    print(triple[0], triple[1])

print(strongly_connected_components(g))
print("\n\n")
