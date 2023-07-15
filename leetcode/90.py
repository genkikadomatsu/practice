# Subsets II
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()        
        subsets = []


        def backtrack(current_subset, i):
            
            if i == len(nums):
                subsets.append(current_subset[:])
                return

            backtrack(current_subset + [nums[i]], i + 1)
            
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
                # This loops ends with i at the last dupe's index
            
            backtrack(current_subset, i + 1) # Skip over the dupe

        backtrack([], 0)
        return subsets


print(Solution().subsetsWithDup([1, 1, 3]))