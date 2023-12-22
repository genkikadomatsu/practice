"""300"""
from typing import List
from math import inf

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Returns the length of the longest increasing subsequence."""

        # this is the O(n^2) solution, there is an O(n log n) solution as well

        dp = [(1, v) for i, v in enumerate(nums)]
        dp[-1] = (1, nums[-1]) # (length, min value)

        for i in reversed(range(len(nums) - 1)):
            for j in range(i + 1, len(dp)):
                if dp[i][1] < dp[j][1] and dp[i][0] < dp[j][0] + 1:
                    dp[i] = (dp[j][0] + 1, dp[i][1])
    
        return max(e[0] for e in dp)