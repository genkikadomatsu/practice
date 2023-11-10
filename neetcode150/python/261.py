"""LeetCode 261 (LintCode)"""
from typing import List

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        """Given an undirected graph, returns True if it is a tree."""

        graph = [i for i in range(n)]

        def union(elem_a, elem_b):
            graph[find(elem_a)] = find(elem_b)            

        def find(elem):
            if graph[elem] == elem:
                return elem
            
            representative_elem = graph[elem] = find(graph[elem])
            return representative_elem

        # Checking that the graph is acyclical
        for a, b in edges:
            if find(a) == find(b):
                return False
            else:
                union(a, b)

        # Checking that the graph is connected
        groups = set()

        for i in range(n):
            groups.add(find(i))

        if len(groups) > 1:
            return False

        return True 
