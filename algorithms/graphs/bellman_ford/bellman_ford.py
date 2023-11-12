"""Example implementation of the Bellman Ford algorithm."""

from math import inf

def bellman_ford(num_vertices: int, source: int, edges: list[list[int]]):
    """
    Given number of nodes and edges of a graph, perform Bellman-Ford and
    print the optimal distaces.

    Vertices are labeled 0 to num_vertices - 1 and edges are formatted like so:
    [[source, destination, distance], [other_source, other_destination, distance], ... ]
    """
    
    optimal_distances = [inf if n != source else 0 for n in range(num_vertices)]

    # Find optimal paths    
    for i in range(num_vertices):
        for source, dest, dist in edges:
            if optimal_distances[dest] > optimal_distances[source] + dist:
                # relax
                optimal_distances[dest] = optimal_distances[source] + dist
 
    # Update negative cycles with negative inf
    for i in range(num_vertices):
        for source, dest, dist in edges:
            if optimal_distances[dest] > optimal_distances[source] + dist:
                optimal_distances[dest] = -inf

    print(optimal_distances)

n = 10
source = 0
edges = [
    [0, 1, 5],
    [1, 6, 60],
    [1, 5, 30],
    [1, 2, 20],
    [2, 3, 10],
    [3, 2, -15],
    [2, 4, 75],
    [4, 9, 100],
    [5, 6, 5],
    [5, 8, 50],
    [5, 4, 25],
    [6, 7, -50],
    [7, 8, -10]
]

bellman_ford(n, source, edges)