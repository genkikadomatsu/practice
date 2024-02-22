# LeetCode 78 - Subsets
from typing import List

# Recursive
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        maxlen = len(nums) 

        def recurse(i, current_subset): 
            nonlocal nums 

            if maxlen == i: 
                nonlocal result 
                result.append(current_subset) 
                return

            recurse(i + 1, current_subset) 
            recurse(i + 1, current_subset + [nums[i]])
            return

        recurse(0, []) 
        return result 

# Iterative
class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Return the powerset (all subsets) of nums."""

        subsets = [[]]
        
        for n in nums:
            new_subsets = [s + [n] for s in subsets] 
            subsets += new_subsets
        
        return subsets
