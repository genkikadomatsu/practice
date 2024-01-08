"""42"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        overall_max = max(height)
        max_index = height.index(overall_max)
        result, current_max = 0, 0

        for h in height[:max_index]:
            current_max = max(h, current_max)
            result += current_max - h

        current_max = 0 
        
        for i in range(len(height) - 1, max_index, -1):
            current_max = max(height[i], current_max)
            result += current_max - height[i]

        return result
