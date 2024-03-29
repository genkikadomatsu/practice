"""55"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if not nums:
            return True

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            goal = i if i + nums[i] >= goal else goal

        return goal == 0 
