


def bs(nums, target):

    low, high = 0, len(nums) - 1

    while low <= high:

        mid = (low + high) // 2

        if target < nums[mid]:
            high = mid - 1
        
        elif target > nums[mid]:
            low = mid + 1
        
        else:
            return True
    
    return False





a = [1,2,3,4,5,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9,10]

print("this should be true", bs(a, 4))
print("this should be true", bs(a, 2))
print("this should be true", bs(a, 7))
print("this should be true", bs(a, 9))
print("this should be true", bs(b, 4))
print("this should be true", bs(b, 2))
print("this should be true", bs(b, 7))
print("this should be true", bs(b, 9))
print("this should be false", bs(b, 11))
