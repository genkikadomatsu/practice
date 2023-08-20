"""LeetCode 347: Top K Frequent Elements

Given some arbitrary list of numbers, nums, and an integer, k, return the k most
frequent elements of nums.
"""
from typing import List

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Returns the k most frequent elements of nums in O(n) avg case time.

        :param nums: List of elements from which we want the k most frequent.
        :param k: The number of elements to return. 
        """
        
        # Get the frequencies of each element.
        counts = {}
         
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        # Here we use list comprehension instead of [[]] * len(nums) because we
        # need each list to be a distinct object in memory.
        elements_by_count = [[] for _ in nums]

        # Insert the elements into the list by their frequency.
        for n, c in counts.items():
            elements_by_count[c - 1].append(n)

        # Return k last elements of flattened list.
        return [item for sublist in elements_by_count for item in sublist][-k:]
