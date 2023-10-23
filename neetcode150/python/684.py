"""LeetCode 684"""
from typing import List

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """Find redundant connections in a graph."""

        n = len(edges)
        parents = [n for n in range(n)] # 0-first indexed (problem is 1-first)

        def find(elem):
            """Given an element, returns the representative element."""

            if parents[elem] == elem:
                return elem
            
            parent = parents[elem] = find(parents[elem]) # path compression

            return parent
    
        def union(elem_a, elem_b):
            """Given two elements, merges their groups."""
            
            parent_a, parent_b = find(elem_a - 1), find(elem_b - 1)
            parents[parent_b] = parent_a

        candidate_solution = None

        for edge in edges:
            node_a, node_b = edge
            
            if find(node_a - 1) != find(node_b - 1):
                union(node_a, node_b)
            else:
                candidate_solution = edge
        
        return candidate_solution
                       