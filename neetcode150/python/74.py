# LeetCode 74
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n
        true_index = lambda x: (x // n, x % n)

        while l <= r:
            mid = (l + r) // 2
            x, y = true_index(mid)

            if not (x < m and y < n):
                return False

            val = matrix[x][y] 

            if target < val:
                r = mid - 1
            elif val < target:
                l = mid + 1
            else:
                return True
        
        return False
                