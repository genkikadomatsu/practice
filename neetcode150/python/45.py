"""45"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        num_jumps, left, right = 0, 0, 0

        while right < len(nums) - 1:

            new_right = right

            for i in range(left, right + 1):
                new_right = max(i + nums[i], new_right)

            left, right, num_jumps = right + 1, new_right, num_jumps + 1

        return num_jumps