from operator import ge


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        

        results = []

        # recursive dfs exploration on the binary decision tree
        def get_subsets(temp, i):
            
            # base case
            if i >= len(nums):
                results.append(temp.copy())
                return
            
            # recursive case (don't add)
            get_subsets(temp, i + 1)

            # recursive case (add)
            temp.append(nums[i])
            get_subsets(temp, i + 1)
            temp.pop()
            return
        
        
        get_subsets([], 0)
        return results




input1 = [1]
input2 = [1, 2]
input3 = [1, 2, 3]

sol = Solution()

print("[1] ->", sol.subsets(input1), end="\n"*2)
print("[1, 2] ->", sol.subsets(input2), end= "\n"*2)
print("[1, 2, 3] ->", sol.subsets(input3), end= "\n"*2)

# Number of Submissions:

