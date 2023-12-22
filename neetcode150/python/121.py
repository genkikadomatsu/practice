"""121"""
from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_gain = 0
        buy_price = inf

        for p in prices:
            buy_price = min(p, buy_price)
            max_gain = max(p - buy_price, max_gain)
        
        return max_gain