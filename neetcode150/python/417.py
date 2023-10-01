"""417 Pacific Atlantic Water Flow"""
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Returns a list of coordinates that represent all spaces on the island
        where rain water can reach both the Pacific and Atlantic Oceans.
        """

        m, n = len(heights), len(heights[0])

        def can_reach(x: int, y: int) -> bool:
            """Returns True if (x, y) can flow to both oceans."""

            reaches_pacific = x == 0 or y == 0
            reaches_atlantic = x == m - 1 or y == n - 1

            dfs_stack = [(x, y)]
            visited = set()

            while dfs_stack:
                x, y = dfs_stack.pop()
               
                neighbors = [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y + 1),
                    (x, y - 1)
                ]

                for neighbor in neighbors:
                    nx, ny = neighbor
                    if (
                        0 <= nx < m and
                        0 <= ny < n and
                        neighbor not in visited and
                        heights[nx][ny] <= heights[x][y]
                    ):
                        if nx == 0 or ny == 0:
                            reaches_pacific = True
                       
                        if nx == m - 1 or ny == n - 1:
                            reaches_atlantic = True
                        
                        visited.add(neighbor)
                        dfs_stack.append(neighbor)

            return reaches_pacific and reaches_atlantic

        result = [] 

        for i in range(m):
            for j in range(n):
                print(i, j)
                if can_reach(i, j):
                    result.append([i, j])

    
        return result
"""417 Pacific Atlantic Water Flow"""
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Returns a list of coordinates that represent all spaces on the island
        where rain water can reach both the Pacific and Atlantic Oceans.
        """

        m, n = len(heights), len(heights[0])

        def can_reach(x: int, y: int) -> bool:
            """Returns True if (x, y) can flow to both oceans."""

            reaches_pacific = x == 0 or y == 0
            reaches_atlantic = x == m - 1 or y == n - 1

            dfs_stack = [(x, y)]
            visited = set()

            while dfs_stack:
                x, y = dfs_stack.pop()
               
                neighbors = [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y + 1),
                    (x, y - 1)
                ]

                for neighbor in neighbors:
                    nx, ny = neighbor
                    if (
                        0 <= nx < m and
                        0 <= ny < n and
                        neighbor not in visited and
                        heights[nx][ny] <= heights[x][y]
                    ):
                        if nx == 0 or ny == 0:
                            reaches_pacific = True
                       
                        if nx == m - 1 or ny == n - 1:
                            reaches_atlantic = True
                        
                        visited.add(neighbor)
                        dfs_stack.append(neighbor)

            return reaches_pacific and reaches_atlantic

        result = [] 

        for i in range(m):
            for j in range(n):
                print(i, j)
                if can_reach(i, j):
                    result.append([i, j])

    
        return result
