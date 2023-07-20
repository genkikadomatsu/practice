"""LeetCode 79 Word Search"""
from collections import deque
from typing import List

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        path = set()

        def starts_word(x: int, y: int, index: int) -> bool:
            
            # Terminal invalid cases
            if (index == len(word) or # out of range index
                not (0 <= x < m and 0 <= y < n) or # out of range position
                board[x][y] != word[index] or # not matching character
                (x, y) in path # already in the path
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

example_input = (
    [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]],
    "SEE"
) # True

failed_first_try_input = (
    [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    "ABCCED"
) # True

failed_second_attempt = (
    [["A","B","C","E"],
     ["S","F","E","S"],
     ["A","D","E","E"]],
    "ABCESEEEFS"
) # True

print(Solution().exist(*failed_second_attempt))
