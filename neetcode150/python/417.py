"""417 Pacific Atlantic Water Flow"""
from typing import List

class Solution:
    def optimal_pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """Optimal solution that has linear average case time complexity."""

        # Working the matrix
        m, n = len(heights), len(heights[0])
        first_row = [(0, i) for i in range(n)]
        last_row = [(m - 1, i) for i in range(n)]
        first_column = [(i, 0) for i in range(m)]
        last_column = [(i, n - 1) for i in range(m)]

        # Get all elements initially touching oceans
        pacific_flow = set(first_row + first_column)
        atlantic_flow = set(last_row + last_column)

        # DFS to find other elements that are touching either
        def dfs(dfs_stack, visited_set): 
            """Explore any nodes that are of equal or taller height."""

            while dfs_stack:
                i, j = dfs_stack.pop()
                neighbors = [
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                ]
                in_range = lambda x, y: (0 <= x < m) and (0 <= y < n)
                flowing = lambda x, y: heights[x][y] >= heights[i][j]
                not_visited = lambda x, y: (x, y) not in visited_set

                for x, y in neighbors:
                    if not_visited(x, y) and in_range(x, y) and flowing(x, y):
                        visited_set.add((x, y))
                        dfs_stack.append((x, y))
                
        dfs(list(pacific_flow), pacific_flow)
        dfs(list(atlantic_flow), atlantic_flow)

        return pacific_flow.intersection(atlantic_flow)


    def naive_pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """Naive solution that has O(n^2) time complexity.

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