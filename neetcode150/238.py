from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:

    prefix = [nums[0]]

    prenums = nums[1:]

    for n in prenums:
        prefix.append(prefix[-1] * n)
    
    postfix = [nums[-1]]

    postnums = nums[:-1]
    postnums.reverse()

    for n in postnums:
        postfix.append(postfix[-1] * n)
    
    postfix.reverse()

    result = []

    for i in range(len(nums)):

        if i == 0:
            result.append(postfix[1])
        elif i == len(nums) - 1:
            result.append(prefix[-2])
        else:
            result.append(prefix[i - 1] * postfix[i + 1])

    return result

print(productExceptSelf([1,2,3]))
