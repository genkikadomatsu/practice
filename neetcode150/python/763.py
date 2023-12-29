"""763"""
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        partitions = []
        partition_ranges = [None for _ in range(len(s))]
        starting_points = {} # O(26)

        # Explore partitions
        for i, c in enumerate(s):
            starting_points[c] = starting_points.get(c, i)
            partition_ranges[i] = (starting_points[c], i)

        # Merge partitions
        current_partition_size = 0
        goal_starting_point = partition_ranges[-1][0]
        
        for i in reversed(range(len(s))):
            current_partition_size += 1
            goal_starting_point = min(partition_ranges[i][0], goal_starting_point)
           
            if goal_starting_point == i:
                partitions.append(current_partition_size)
                current_partition_size = 0

        partitions.reverse()
        return partitions
