"""309"""
from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        BOUGHT = 0
        SOLD = 1
        COOLING = 2

        n = len(prices)
        table = [[None for _ in range(n + 1)] for _ in range(3)]
        table[BOUGHT][0], table[SOLD][0], table[COOLING][0] = -inf, 0, 0

        for i in range(1, n + 1):
            j = i - 1
            table[BOUGHT][i] = max(table[COOLING][j] - prices[j], table[BOUGHT][j])
            table[SOLD][i] = prices[j] + table[BOUGHT][j]
            table[COOLING][i] = max(table[SOLD][j], table[COOLING][j])

        return max(table[BOUGHT][-1], table[SOLD][-1], table[COOLING][-1])