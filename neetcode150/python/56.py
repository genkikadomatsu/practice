"""56"""
from typing import List
from math import inf

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        result = []

        # O(nlogn) sort intervals based on starting index
        intervals = sorted(intervals, key=lambda l: l[0], reverse=False)
        should_merge = lambda a, b: a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1] 
        merge = lambda a, b: [min(a[0], b[0]), max(a[1], b[1])]
        current_interval = intervals[0]

        for interval in intervals[1:]:
        
            if should_merge(current_interval, interval):
                current_interval = merge(current_interval, interval)
            else:
                result.append(current_interval)
                current_interval = interval
            

        result.append(current_interval)
        return result 