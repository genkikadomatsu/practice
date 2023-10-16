"""LeetCode 323"""
from typing import List

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        """Returns the number of connected components in the graph."""

        parents = [i for i in range(n)]
        num_components = n

        def find(a):
            """Returns the representative element of a group."""

            if a != parents[a]:
                a = parents[a] = find(parents[a])
            
            return a 

        def union(a, b):
            """Union the two groups of the two elements."""

            parents[find(a)] = parents[find(b)]      

       
        for edge_a, edge_b in edges:
            if find(edge_a) != find(edge_b):
                num_components -= 1
                union(edge_a, edge_b)
        
        return num_components
