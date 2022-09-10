class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)
        results = [[]]

        for i in range(n):
            j = len(results)
            for k in range(j):
                new_element = results[k].copy()
                new_element.append(nums[i])
                results.append(new_element)
        
        return results

input1 = [1]
input2 = [1, 2]
input3 = [1, 2, 3]

sol = Solution()
print("[1] ->", sol.subsets(input1), end="\n"*2)
print("[1, 2] ->", sol.subsets(input2), end= "\n"*2)
print("[1, 2, 3] ->", sol.subsets(input3), end= "\n"*2)