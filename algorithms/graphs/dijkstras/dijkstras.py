"""Dijkstra's Algorithm

Dijkstra's algorithm is a single source shortest path algorithm that has a time
complexity of O(E + V log V) and a space complexity of O(V + E). Dijkstra's only
works on non-negative weighted graphs.
"""
import heapq
from math import inf
from weighted_node import WeightedNode

def dijkstras(
    graph: list[WeightedNode],
    source: int
) -> None:
    """Prints shortest path from source to all nodes in the graph.
    
    The graph is guaranteed to be non-negative weighted, and the input graph's
    node ID's match their index in the adjacency list
    """

    # Initialize the distance array and priority queue
    distances = [inf for _ in graph]
    parents = [None for _ in graph]
    pq = []

    for node in graph:
        distances[node.id] = inf
        if node.id == source:
            distances[node.id] = 0 # source node's distance to source node is 0
            parents[node.id] = node.id
            pq.append((0, node)) # (distance from source, node)

    # Find shortest paths
    while pq:
        dist_to_source, node = heapq.heappop(pq)

        for nb, dist_to_nb in node.neighbors:
            new_dist = dist_to_nb + dist_to_source
            
            if new_dist < distances[nb.id]:
                distances[nb.id] = new_dist
                parents[nb.id] =  node.id
                heapq.heappush(pq, (new_dist, nb))
    
    # Print paths
    for node in graph:
        print(node.id, "<-", end="")
        current_node_id = parents[node.id]
        while current_node_id != source:
            print(current_node_id, "<-", end="")
            current_node_id = parents[current_node_id]
        print(source)

# Print example
from example_graphs import graph_1
dijkstras(graph_1, 0)
