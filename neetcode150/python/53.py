"""53"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = 0
        running_sum = 0

        for n in nums:
            running_sum = running_sum + n if running_sum > 0 else n
            max_sum = max(max_sum, running_sum)

        return max_sum