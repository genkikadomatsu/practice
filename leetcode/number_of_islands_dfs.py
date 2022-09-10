class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        island_count = 0
        dfs_stack = []
        visited = set()
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            visited.add((x, y))
            dfs_stack.append((x , y))

          
            
            while dfs_stack:
                curr = dfs_stack.pop()
                neighbors = [[curr[0] + 1, curr[1]],
                             [curr[0] - 1, curr[1]],
                             [curr[0], curr[1] + 1],
                             [curr[0], curr[1] - 1]]  
                for nx, ny in neighbors:
                    if nx not in range(m) or ny not in range(n):
                        pass
                    elif grid[nx][ny] == "1" and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        dfs_stack.append((nx, ny))
                
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island_count += 1
                    dfs(i, j)
        
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