"""LeetCode 210"""
from typing import List

# Example inputs
# 8, [[0, 1], [7, 6]]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Returns topological sort of courses (based on prerequisites).
        :param numCourses: There are courses labeled 0 to n - 1.
        :param prerequisites: List of course prerequisites.

        Course prerequisites are represented as such for
            course 0 being a prerequisite of course number 1, and
            course 2 being a reprequisites of cousrse number 4. 
                numCourses = 5
                prerequisites = [[1, 0]], [4, 2]]
        """

        # Adjacency list
        graph = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            course, dependency = prerequisite[0], prerequisite[1]
            graph[dependency].append(course)

        reversed_top_sort = []
        visited = set()
        current_recursion_stack = set()

        # Topological sort
        def dfs(node): 
            if node in current_recursion_stack:
                raise Exception("Found a cyclical dependency!!!")

            current_recursion_stack.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

            visited.add(node)
            reversed_top_sort.append(node)

        random = 0
        
        while len(visited) < numCourses:
            
            while random in visited:
                random += 1

            try: 
                dfs(random)
            except Exception:
                return []

        reversed_top_sort.reverse() 
        return reversed_top_sort
