from typing import List


def num_islands(grid: List[List[str]]) -> int:
	if not grid:
		return 0
	num_island, R, C = 0, len(grid), len(grid[0])

	# Thinking is :
	# 1. If encounter a 1, start a DFS and find all the connected component. This will represent an island
	# 2. be careful to mark all the visted with an separate character to avoid duplicate count
	# 3. Iterate through the grid

	def dfs(r, c):
		if r < 0 or r > R - 1 or c < 0 or c > C - 1 or grid[r][c] == "0":
			return 0
		grid[r][c] = "0"
		dfs(r + 1, c)
		dfs(r - 1, c)
		dfs(r, c + 1)
		dfs(r, c - 1)
		return 1

	for i in range(R):
		for j in range(C):
			if grid[i][j] == "1":
				num_island += dfs(i, j)
	return num_island


input1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
input2 = [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]

print(num_islands(input1))
print(num_islands(input2))