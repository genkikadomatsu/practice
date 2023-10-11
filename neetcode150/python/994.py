"""LeetCode 994"""
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten_oranges = deque()
        m, n = len(grid), len(grid[0])
        any_fresh = False

        # Find the oranges that are rotten at time=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))
                elif not any_fresh and grid[i][j] == 1:
                    any_fresh = True
        

        # If there aren't any rotten or fresh oranges, we return 0 
        if not bool(rotten_oranges) and not any_fresh:
            return 0
        
        time = -1
        
        while rotten_oranges:
            
            for _ in range(len(rotten_oranges)):
                i, j = rotten_oranges.popleft()
                neighbors = [
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1)
                ]

                in_range = lambda a, b: 0 <= a < m and 0 <= b < n
                is_rotten = lambda a, b: grid[a][b] == 1

                for i, j in neighbors:
                    if in_range(i, j) and is_rotten(i, j):
                        grid[i][j] = 2
                        rotten_oranges.append((i, j))

            time += 1

        # Check if there are any remainder fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return time

        