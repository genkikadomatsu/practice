from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        combinations = []

        def bt(
            curr_combo: list[int],
            i: int,
            curr_sum: int
        ) -> None:

             
            if curr_sum == target:
                combinations.append(curr_combo[:])
                return

            if i == len(candidates) or curr_sum > target:
                return
          
            bt(curr_combo + [candidates[i]], i + 1, curr_sum + candidates[i]) 
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            
            bt(curr_combo, i + 1, curr_sum) 
            return

        bt([], 0, 0)
        return combinations

print(Solution().combinationSum2([2, 1, 5, 2, 2], 5))
# Should be [[1, 2, 2], [5]]