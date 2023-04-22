
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    
    
    permutations = []

    if len(nums) <= 1:
        return [nums]
    
    for i in range(len(nums)):

        sub_nums = nums.copy()
        removed_element = sub_nums.pop(i)
        sub_permutations = permute(sub_nums)
        new_permutations = []
        for sp in sub_permutations:
            new_permutation = sp + [removed_element]
            print(new_permutation)
            new_permutations.append(new_permutation)
        permutations.extend(sub_permutations)
    
    return permutations
    


print(permute([1, 2]))