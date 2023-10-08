"""LeetCode 130"""
from typing import List

class Solution:


    def solve(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""

        m, n = len(board), len(board[0])

        def DFS(i: int, j: int):
            """Perform DFS on an X element and return the entire region.
            
            For this problem in particular, we mark elements with 'G' if they're
            visited. 
            """

            dfs_stack = [(i, j)]
            board[i][j] = "G"
            
            in_range = lambda a, b: 0 <= a < m and 0 <= b < n
            is_O = lambda a, b: board[a][b] == "O"

            while dfs_stack:
                i, j = dfs_stack.pop()
                neighbors = [
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1)
                ]

                for i, j in neighbors:
                    if in_range(i, j) and is_O(i, j):
                        dfs_stack.append((i, j))
                        board[i][j] = "G"
        
        # Get bordering elements
        top = [(0, j) for j in range (n)]
        bottom = [(m - 1, j) for j in range(n)]
        left = [(i, 0) for i in range(m)]
        right = [(i, n - 1) for i in range(m)]
        border = set(top + bottom + left + right)

        # Mark regions as "G" for now so we can update board in O(n) worst case
        for i, j in border:
            if board[i][j] == "O":
                DFS(i, j)

        # Update board 
        for i in range(m):
            for j in range(n):
                if board[i][j] == "G":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

input = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]
Solution().solve(input)