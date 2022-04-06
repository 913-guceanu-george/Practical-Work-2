# Practical work 2 --- Graph Algo

Due: week 7-8.

Solve the assigned problem from those below. Additionaly, you may solve one or more of the bonus problems at the end of the page. Use the abstract data type created for lab. 1; modify it if necessary.

## Assigned problems

1. Write a program that, given a directed graph and two vertices, finds a lowest length path between them, by using a forward breadth-first search from the starting vertex.

2. Write a program that, given a directed graph and two vertices, finds a lowest length path between them, by using a backward breadth-first search from the ending vertex.

3. Write a program that finds the connected components of an undirected graph using a depth-first traversal of the graph.

4. Write a program that finds the connected components of an undirected graph using a breadth-first traversal of the graph.

## Optional, "bonus" problems

1B. Write a program that finds the strongly-connected components of a directed graph in O(n+m) (n=no. of vertices, m=no. of arcs)

2B. Write a program that finds the biconnected components of an undirected graph in O(n+m).

3B. Use a lowest length path algorithm and a new implementation of the interface from lab 1 to solve any of the following problems:

Wolf, goat and cabbage problem: A man has a wolf, a goat and a cabbage and must cross a river in a boat than can hold him and only one of the three items. He cannot leave alone the wolf with the goat or the goat with the cabbage. Find a shortest sequence of moves for crossing the river.
Cannibals and missionairs: Three cannibals and three missionairs must cross a river using a boat that can carry at most two people. It is not allowed to have, at any moment and on any bank, the missionairs outnumbered by the cannibals (unless no missionairs exist on that bank at that time). Again, find a shortest sequence of moves for crossing the river.
Jealous husbands: Three married couples must cross a river, using a using a boat that can carry at most two people. It is not allowed that any woman be, on a bank or on the boat, in the presence of a man, unless her husband is at the same place. Again, find a shortest sequence of moves for crossing the river.
4B. Similarly with 3B, solve the 15 puzzle.
