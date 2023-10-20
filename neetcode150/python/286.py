"""LeetCode 286"""
from typing import List
from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: None
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        
        m, n = len(rooms), len(rooms[0])
        GATE, WALL, EMPTY = 0, 1, 2147483647
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == GATE:
                    queue.append((i, j))
        
        in_range = lambda x, y: 0 <= x < m and 0 <= y < n
        not_gate_or_wall = lambda x, y: rooms[x][y] not in [GATE, WALL]

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                distance = rooms[i][j]
                neighbors = [
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1)
                ]
                for i, j in neighbors:
                    if in_range(i, j) and not_gate_or_wall(i, j):
                        if rooms[i][j] == 0 or rooms[i][j] > distance + 1:
                            rooms[i][j] = distance + 1
                            queue.append((i, j))

        return