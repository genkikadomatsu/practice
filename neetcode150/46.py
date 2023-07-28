# Intuitive Solution
from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        """Returns the symmetric group of nums."""

        permutations = []

        def backtrack(current_permutation: List[int], remainder: List[int]) -> None:
            """Backtrack."""
            
            if not remainder:
                permutations.append(current_permutation[:])

            for _ in range(len(remainder)):
                current_permutation.append(remainder.pop(0))
                backtrack(current_permutation, remainder)
                remainder.append(current_permutation.pop())
        
        backtrack([], nums)
        return permutations


# class Solution:

#     def permute(self, nums: List[int]) -> List[List[int]]:
#         """Returns all possible permutations of the input list."""

#         permutations = []

#         if not nums or len(nums) == 1:
#             return [nums[:]]

#         for i in range(len(nums)):
#             n = nums.pop(0)
#             subpermutations = self.permute(nums)
#             permutations.extend([sp + [n] for sp in subpermutations])
#             nums.append(n)

#         return permutations

print(Solution().permute([1, 2]))