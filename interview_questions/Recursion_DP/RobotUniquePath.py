
# DP problem find the total number of unique paths from top left to bottom right corner - LC 62
def robot_unique_paths(m: int, n: int) -> int:
	if m < 1 or n < 1:
		return 0
	# matrix to store the dp numbers
	result_dp = [[0 for _ in range(0, n)] for _ in range(0, m)]

	# fill the 1st row and the first column
	for i in range(0, n):
		result_dp[0][i] = 1

	for i in range(0, m):
		result_dp[i][0] = 1

	# the cell can have the counts from left or top unique ways
	for i in range(1, m):
		for j in range(1, n):
			result_dp[i][j] = result_dp[i - 1][j] + result_dp[i][j - 1]

	return result_dp[m - 1][n - 1]


print("Unique paths for a 3 X 2 grid from Start to Finish - ",robot_unique_paths(3,2))
print(" ")
print("Unique paths for a 7 X 3 grid from Start to Finish - ",robot_unique_paths(7,3))


