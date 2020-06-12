from typing import List


def unique_paths_obstacles(obstacleGrid: List[List[int]]) -> int:
	if obstacleGrid is None or len(obstacleGrid) == 0:
		return 0
	# fill in first row and make obstacles some other value
	m = len(obstacleGrid)
	n = len(obstacleGrid[0])
	result_dp = [[0 for _ in range(0, n)] for _ in range(0, m)]

	# Edge cases (1) either 1st square and last square are blocked , so we can't start or reach the end, hence return 0
	# (2)
	# go over the 1st row
	for i in range(0, n):
		if obstacleGrid[0][i] == 1 or (i > 0 and result_dp[0][i - 1] == "X"):
			result_dp[0][i] = "X"
		else:
			result_dp[0][i] = 1

	# go over the 1st column
	for i in range(0, m):
		if obstacleGrid[i][0] == 1 or (i > 0 and result_dp[i - 1][0] == "X"):
			result_dp[i][0] = "X"
		else:
			result_dp[i][0] = 1

	# loop over the grid to find the number of unique ways
	for i in range(1, m):
		for j in range(1, n):
			if obstacleGrid[i][j] == 1:
				result_dp[i][j] = "X"
				continue
			else:
				left_value = 0
				top_value = 0
				if result_dp[i - 1][j] != "X":
					top_value = result_dp[i - 1][j]
				if result_dp[i][j - 1] != "X":
					left_value = result_dp[i][j - 1]
				result_dp[i][j] = left_value + top_value

	return result_dp[m - 1][n - 1]


matr = [[0,0,0],[0,1,0],[0,0,0]]
matr1 = [[0,0],[1,1],[0,0]]

# print(unique_paths_obstacles(matr))
print(unique_paths_obstacles(matr1))