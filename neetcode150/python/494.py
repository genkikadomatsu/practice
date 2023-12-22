"""494"""
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        sum_all = sum(nums)
       
        if target > sum_all:
            return 0

        table = [[0 for _ in range(len(nums))] for _ in range(-sum_all, sum_all + 1)]
        conceptual_index = lambda i: i + sum_all
        
        table[conceptual_index(nums[0])][0] += 1
        table[conceptual_index(-nums[0])][0] += 1
        
        for j in range(1, len(nums)):
            for i in range(-sum_all, sum_all + 1):
                real_index = conceptual_index(i)
                
                if 0 < real_index - nums[j]: 
                    table[real_index][j] += table[real_index - nums[j]][j - 1]
                
                if real_index + nums[j] < len(table):
                    table[real_index][j] += table[real_index + nums[j]][j - 1]

                if nums[j] == 0:
                    table[real_index][j] = table[real_index][j - 1] * 2

        return table[conceptual_index(target)][-1]