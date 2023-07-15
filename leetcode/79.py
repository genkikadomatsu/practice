# LeetCode 79, Word Search
from collections import deque
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Returns True if word exists in board."""

        m, n = len(board), len(board[0])
        

        for y in range(m):
            for x in range(n):
                if explore(x, y):
                    