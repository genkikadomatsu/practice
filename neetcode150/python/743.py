"""743"""
from typing import List
import heapq
from math import inf

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        times: list of edges (source, target, weight)
        n: number of nodes
        k: the source node
        """

        # Construct graph
        graph = [[] for _ in range(n)] # [[(destination node, weight)]]

        for source, target, weight in times:
            source = source - 1
            target = target - 1
            graph[source].append((target, weight))
        
        # Dijkstra's
        pq = [(k - 1, 0)]
        distances = [0 if i == k - 1 else inf for i in range(n)]
        parents = [k - 1 if i == k - 1 else None for i in range(n)]

        while pq:
            node, distance = heapq.heappop(pq)

            for neighbor, weight in graph[node]:
                if distance + weight < distances[neighbor]:
                    distances[neighbor] = distance + weight
                    parents[neighbor] = node
                    heapq.heappush(pq, (neighbor, distances + weight))
        
        return max(distances) if inf not in distances else -1