
# Search in a sorted Matrix where both rows and columns are sorted - LC 74, LC 240
def search_matrix(matrix, target):
	"""
	:type matrix: List[List[int]]
	:type target: int
	:rtype: bool
	"""
	if not matrix:
		return False
	len_rows = len(matrix)
	len_cols = len(matrix[0])
	if len_rows == 0 or len_cols == 0:
		return False
	elif len_rows == 1 and len_cols == 1:
		if target == matrix[0][0]:
			return True
		else:
			return False
	else:
		row, col = 0, len_cols - 1
		while row <= len_rows-1 and col >= 0:
			if matrix[row][col] == target:
				return True
			elif matrix[row][col] > target:
				col -= 1
			else:
				row += 1
		return False


# input = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# targ = 5

# input = [[-1,3]]
# targ = -1

input = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
targ = 20

print(search_matrix(input, targ))