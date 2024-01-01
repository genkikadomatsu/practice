"""48"""
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        m, n = len(matrix), len(matrix[0]) 
        corners = [(0, n - 1), (m - 1, n - 1), (m - 1, 0), (0, 0)]
        i_iters = m // 2 if m % 2 == 0 else (m // 2) + 1
        j_iters = n // 2

        for i in range(i_iters):
            for j in range(j_iters):
                v_dist, h_dist = i - 0, j - 0
                temp = matrix[i][j]
        
                for c in corners:
                    y = c[0] + h_dist if c[0] == 0 else c[0] - h_dist
                    x = c[1] + v_dist if c[1] == 0 else c[1] - v_dist
                    matrix[y][x], temp = temp, matrix[y][x]
                    h_dist, v_dist = v_dist, h_dist
    