"""134"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        tank = 0
        start_point = 0

        for i in range(len(gas)):

            tank = tank + gas[i] - cost[i]
            
            if tank < 0:
                start_point += 1
                tank = 0
            
        return start_point if start_point < len(gas) else -1 

print(Solution().canCompleteCircuit([0, 0, 0, 3, 4], [3, 2, 2, 0, 0]))