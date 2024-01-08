"""167"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            print(total)
            if total == target:
                return [left + 1, right + 1]
            
            if total < target:
                left += 1
            elif total > target:
                right -= 1

print(Solution().twoSum([2,7,11,15], 9))