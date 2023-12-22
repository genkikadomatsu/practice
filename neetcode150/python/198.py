"""198 House Robber"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """Returns the maximum profit possible from robbing the houses."""

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
    
        profits = [0 for _ in range(len(nums))]

        profits[0], profits[1], profits[2] = nums[0], nums[1], nums[0] + nums[2]

        for i in range(3, len(nums)):
            profits[i] = nums[i] + max(profits[i - 2], profits[i - 3])
        
        return max(profits[-1], profits[-2])
