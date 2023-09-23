"""Quicksort implementation

Quicksort is a O(n^2) worst case O(nlogn) expected case time complexity sort
algorithm. To perform quicksort, we first arbitrarily pick some pivot element.
Then, we parition the array into two parts,
1. elements whose value is lesser than the pivot, and
2. elements whose value is greater than the pivot.
Then, we recursively sort the two partitions and concatenate them after.
"""

def quicksort(nums: list[int]) -> list[int]:
    """Returns the sorted input list."""
    # Base cases
    if not nums:
        return []

    if len(nums) == 1:
        return nums

    if len(nums) == 2:
        return [min(nums), max(nums)]
    
    # Pick a pivot
    print(nums)

    pivot = nums.pop()
    lesser = [n for n in nums if n <= pivot]
    greater = [n for n in nums if n > pivot]

    return quicksort(lesser) + [pivot] + quicksort(greater)

def visualize_quicksort(nums: list[int]) -> list[int]:
    """Returns the sorted input list."""
    
    if not nums:
        return []

    if len(nums) == 1:
        return nums

    if len(nums) == 2:
        return [min(nums), max(nums)]
    
    pivot = nums.pop()
    lesser = [n for n in nums if n <= pivot]
    greater = [n for n in nums if n > pivot]
    
    print(f"{lesser}-[{pivot}]-{greater}")
   
    return visualize_quicksort(lesser) + [pivot] + visualize_quicksort(greater)

print(visualize_quicksort([5,4,2,2,1,5,1,3,5,789,67,324,12,1]))