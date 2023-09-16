# LeetCode 207
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Returns true if there's no cycles in prerequisites."""

        # Construct graph as an adjacency list (node to prerequisites)
        adjacency_list = {i:[] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            adjacency_list[course].append(prereq)
        
        visited = set()

        # Perform DFS
        def points_to_visited(node: int) -> bool:
            """
            This node points to an already visited node, or to a path that
            leads to an already visited node.
            """

            # If this node is already visited, this is a cycle.
            if node in visited:
                return True

            # Mark this node as visited.
            visited.add(node)

            # Recursively check if any neighboring nodes are in a cycle.
            for prereq in adjacency_list[node]:
                if points_to_visited(prereq):
                    return True

            # If no cycles, remove this node from the graph (and visited).
            adjacency_list[node] = []
            visited.remove(node)

            return False

        for node in adjacency_list:
            if points_to_visited(node):
                return False
        
        return True
