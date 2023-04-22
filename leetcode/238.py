from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:

    pre, post, result = [nums[0]], [nums[-1]], []

    for i in range(1, len(nums)):
        pre.append(nums[i] * pre[i - 1])

    for i in range(1, len(nums)):
        post.append(nums[-i - 1] * post[i - 1])

    post.reverse()
    print(pre)
    print(post)

    for i in range(len(nums)):
        
        if i == 0:
            result.append(1 * post[i + 1])
        elif i == len(nums) - 1:
            result.append(pre[i - 1] * 1)
        else:
            result.append(pre[i - 1] * post[i + 1])
    
    return result

print(productExceptSelf([1,2,3])) # should be [6, 3, 2]