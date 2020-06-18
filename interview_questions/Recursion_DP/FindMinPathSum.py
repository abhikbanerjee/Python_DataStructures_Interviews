from typing import List


# DP problem find the minimum path sum from top left to bottom right corner - LC 64
def min_path_sum(grid: List[List[int]]) -> int:
	if grid is None or len(grid )==0:
		return 0
	R = len(grid)
	C = len(grid[0])
	result = [[0 for _ in range(C)] for _ in range(R)]
	result[0][0] = grid[0][0]

	# initialize the first row and the first column
	for i in range(1, C):
		result[0][i] = grid[0][i] + result[0][ i -1]
	for i in range(1, R):
		result[i][0] = grid[i][0] + result[ i -1][0]

	# now fill the DP matrix to find out the minimum at each step
	for i in range(1, R):
		for j in range(1,C):
			top_path_sum = grid[i][j ] +result[ i -1][j]
			left_path_sum = grid[i][j ] +result[i][ j -1]
			result[i][j] = min(top_path_sum, left_path_sum)

	# return the sum at the right most cell
	return result[R -1][C -1]


input_1 = [[1,3,1],[1,5,1],[4,2,1]]
print(min_path_sum(input_1))