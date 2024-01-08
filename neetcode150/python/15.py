"""15"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            a, b, c = i, i + 1, len(nums) - 1

            while b < c:

                total = nums[a] + nums[b] + nums[c]

                if total < 0:
                    b += 1
                elif total > 0:
                    c -= 1 
                else:
                    result.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    
                    while b < len(nums) - 1 and nums[b] == nums[b - 1]:
                        b += 1

                    while c > 0 and nums[c] == nums[c + 1]:
                        c -= 1

        return result