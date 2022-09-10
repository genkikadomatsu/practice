from collections import deque

# LeetCode 200
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """Find the number of islands in grid."""

        island_count = 0
        visited = set()
        m, n = len(grid), len(grid[0])


        # run bfs
        def bfs(x, y):
            bfs_q = deque()
            bfs_q.append((x, y))

            while bfs_q:
                temp = bfs_q.popleft()
                neighbors = [[temp[0] + 1, temp[1]    ],
                             [temp[0] - 1, temp[1]    ],
                             [temp[0]    , temp[1] - 1],
                             [temp[0]    , temp[1] + 1]]
                for nx, ny in neighbors:
                    if (nx not in range(m)) or (ny not in range(n)):
                        pass
                    elif (grid[nx][ny] == "1") and ((nx, ny) not in visited):
                        bfs_q.append((nx, ny))
                        visited.add((nx, ny))


        # run bfs on each unvisited "1"
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == "1") and ((i, j) not in visited):
                    visited.add((i, j))
                    island_count += 1
                    bfs(i, j)
        
        print(island_count)
        return island_count


test_grid_1 = [
    ["1", "0"],
    ["0", "1"]
]

test_grid_2 = [
    ["1", "0"],
    ["1", "1"]
]

test_grid_3 =[
    ["1", "1", "1", "0"],
    ["0", "0", "1", "0"],
    ["1", "1", "1", "1"],
    ["0", "0", "1", "0"],
    ["0", "0", "1", "0"]
]

test_grid_4 =[
    []
]

test_grid_5 =[
    ["1", "1", "0", "0"],
    ["0", "0", "1", "0"],
    ["1", "1", "0", "1"],
    ["0", "0", "1", "0"],
    ["0", "0", "1", "0"]
]
solution = Solution()

solution.numIslands(test_grid_1)
print("Above this should be 2")

solution.numIslands(test_grid_2)
print("Above should be 1")

solution.numIslands(test_grid_3)
print("Above should be 1")

solution.numIslands(test_grid_4)
print("Above should be 0")

solution.numIslands(test_grid_5)
print("Above should be 5")

# Number of Submissions: