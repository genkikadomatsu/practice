"""LeetCode 746"""
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Return the minimum cost to climb to the top of the stairs."""

        if not cost:
            return 0

        min_a, min_b = 0, cost[0]

        for i in range(1, len(cost)):
            min_a, min_b = min_b, cost[i] + min(min_a, min_b)
        
        return min(min_a, min_b)
