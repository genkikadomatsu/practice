# LeetCode 78 - Subsets
from typing import List


# Recursive
class Solution:
    
    def subsets(self, nums):


        subsets = []
        subset = []

        def recurse(i: int):
            if i == len(nums):
                subsets.append(subset[:])
                return

            # Do not include
            recurse(i + 1)

            # Include
            subset.append(nums[i])
            recurse(i + 1)

            subset.pop()
            return
    
        recurse(0)
        return subsets

print(Solution().subsets([1,2,3]))

# Iterative
class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Return the powerset (all subsets) of nums."""

        subsets = [[]]
        
        for n in nums:
            new_subsets = [s + [n] for s in subsets] 
            subsets += new_subsets
        
        return subsets

print(Solution().subsets([1,2,3]))