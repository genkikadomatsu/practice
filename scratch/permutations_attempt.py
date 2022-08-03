class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        
        permutations = []
        
        def dfs(working, remaining):
            
            if not remaining:
                permutations.append(working)
                print(working)
                return
            
            for x in remaining:
                new_working = working.copy()
                new_working.append(x)
                new_remaining = remaining.copy()
                new_remaining.remove(x)
                dfs(new_working, new_remaining)
            
            return
                
        
        for n in nums:
            remainders = nums.copy()
            remainders.remove(n)
            start = [n]
            dfs(start, remainders)
            
        print("solution:", permutations)
        return permutations

sol = Solution()

sol.permute([1, 2, 3])
sol.permute([1,2])
sol.permute([1])
sol.permute([])
