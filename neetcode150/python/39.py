from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combinations = []

        def backtrack(combination: List[int], i: int) -> None:

            if i == len(candidates) - 1:
                return
            
            if sum(combination) == target:
                combinations.append(combination[:])
                return

            if sum(combination) > target:
                return

            backtrack(combination + [candidates[i]], i)
            backtrack(combination, i + 1)
            return
        
        backtrack([], 0)

        return combinations