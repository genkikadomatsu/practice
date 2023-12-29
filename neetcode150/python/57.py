"""57"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        merge = lambda a, b: [min(a[0], b[0]), max(a[1], b[1])]
        should_merge = lambda a, b: a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]
        should_insert = lambda a, b: a[0] < b[0]
        result = []
        current = newInterval

        for i, interval in enumerate(intervals):
            
            if should_merge(current, interval):
                current = merge(current, interval)
                continue

            if should_insert(current, interval):
                result.append(current)
                result.extend(intervals[i:])
                return result
        
            result.append(interval)
        
        return result

            