"""152"""
from math import inf
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Return the maximum product of all subarrays."""

        max_prod = nums[0]
        min_prod = nums[0]
        max_of_all = -inf

        for i in range(1, len(nums)):
            
            prod_with_max = nums[i] * max_prod
            prod_with_min = nums[i] * min_prod

            max_prod = max(nums[i], prod_with_max, prod_with_min)
            min_prod = min(nums[i], prod_with_max, prod_with_min)
            
            max_of_all = max(max_prod, max_of_all)

        return max_of_all



print(Solution().maxProduct([2,3,-2,4]))