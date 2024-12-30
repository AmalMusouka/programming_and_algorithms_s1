# 1. Adjacency Matrix to Adjacency List
# Write a function that takes a undirected graph in adjacency matrix representation, and returns the same graph in adjacency list representation.
#
# Assume that the graph's vertices are numbered from 0 to (V – 1).
#
# 2. Adjacency List to Adjacency Matrix
# Write a function that takes a undirected graph in adjacency list representation, and returns the same graph in adjacency matrix representation.
#
# Assume that the graph's vertices are numbered from 0 to (V – 1).

# 3.Reverse the Direction
# Write a functon that takes a directed graph G in adjacency list representation, with integer vertex ids.
#
# The function should return a graph that is like G, but in which all edges point in the opposite direction.


def to_adj_list(m):
    v = len(m)
    l = [[] for _ in range(v)]
    for i in range(v):
        for j in range(v):
            if m[i][j]:
                l[i].append(j)
    return l

def to_adj_matrix(l):
    v = len(l)
    m = [v * [0] for _ in range(v)]
    for i, edges in enumerate(l):
        for j in edges:
            m[i][j] = 1
    return m

def reverse_graph(l):
    v = len(l)
    rev_l = [[] for _ in range(v)]
    for i, edges in enumerate(l):
        for j in edges:
            rev_l[j].append(i)
    return rev_l

x = [[0, 1, 0, 1],[1, 0, 1, 1],[0, 1, 0, 0],[1, 1, 0, 0]]
print(to_adj_matrix(to_adj_list((x))))