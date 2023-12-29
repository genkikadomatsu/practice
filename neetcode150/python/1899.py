"""1899"""
from typing import List
from math import inf

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        candidate = [-inf, -inf, -inf]

        # Checks if we can use a triplet to merge
        usable = lambda a: (
            a[0] <= target[0] and
            a[1] <= target[1] and
            a[2] <= target[2]
        )

        # Merges two triplets
        merge = lambda a, b: [
            max(a[0], b[0]),
            max(a[1], b[1]),
            max(a[2], b[2])
        ]

        for triplet in triplets:
            if usable(triplet):
                candidate = merge(candidate, triplet)

        return candidate == target
