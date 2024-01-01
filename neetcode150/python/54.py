"""54"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top, left, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        result = []
        i, j = 0, -1
        
        while top <= bottom and left <= right:

            # Go right
            if not j < right:
                break

            while j < right:
                j += 1
                result.append(matrix[i][j])
            top += 1
            
            # Go down
            if not i < bottom:
               break

            while i < bottom:
                i += 1
                result.append(matrix[i][j])
            right -= 1

            # Go left
            if not left < j:
                break
           
            while left < j:
                j -= 1
                result.append(matrix[i][j])
            bottom -= 1

            # Go up
            if not i > top:
                break
            
            while i > top:
                i -= 1
                result.append(matrix[i][j])
            left += 1
        
        return result

Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])