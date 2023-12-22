"""LeetCode 1584 Min Cost to Connect All Points"""
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Given a list of cartesian coordinates, return the MST when all points
        are used to form a fully connected graph. Use manhattan distance when
        calculating distances of edges between points.

        Manhattan distance is:
            |x_1 - x_2| + |y_1 - y_2| = manhattan distance
        """

        # Construct the graph (as an adjacency list)
        N = len(points)
        adj = {i: [] for i in range(N)}  # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        visited = set()
        pq = [[0, 0]]
        min_cost = 0

        while pq:
            cost, node = heapq.heappop(pq)
            if node not in visited:
                min_cost += cost
                visited.add(node)
                for cost, neighbor in adj[node]:
                    if neighbor not in visited:
                        heapq.heappush(pq, [cost, neighbor])

        return min_cost

