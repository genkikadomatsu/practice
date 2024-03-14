"""LeetCode 79 Word Search"""
from typing import List

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        path = set()

        def starts_word(x: int, y: int, index: int) -> bool:
            
            # Terminal invalid cases
            if (index == len(word)
                or not (0 <= x < m and 0 <= y < n)
                or board[x][y] != word[index]
                or (x, y) in path
            ):
               return False
             
            # Terminal valid case
            if index == len(word) - 1:
                return True

            # Recursive cases
            path.add((x, y))

            for neighbor in [
                (x + 1, y, index + 1),
                (x - 1, y, index + 1),
                (x, y + 1, index + 1),
                (x, y - 1, index + 1)
            ]:
                if starts_word(*neighbor):
                    return True
            
            path.remove((x, y))
            return False
             
        for i in range(m):
            for j in range(n):
                if starts_word(i, j, 0):
                    return True

        return False
