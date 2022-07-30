# Backtracking Solution
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        permutations = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            sub_permutations = self.permute(nums)
            
            for sp in sub_permutations:
                sp.append(n)
                
            permutations.extend(sub_permutations)
            nums.append(n)
        
        return permutations

# Number of Submissions: 1

sol = Solution()

print(sol.permute([1, 2, 3]),
sol.permute([1,2]),
sol.permute([1]),
sol.permute([]))
