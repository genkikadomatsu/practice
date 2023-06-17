from typing import List
import math

# LeetCode 739

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0 for t in temperatures]
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                res_index, disregard = stack.pop()
                result[res_index] = i - res_index 
            stack.append((i, t))
        
        return result


while True:
    print(Solution().dailyTemperatures([int(s) for s in input("temps:").split()]))