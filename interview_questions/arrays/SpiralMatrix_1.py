from typing import List


def spiral_order( matrix: List[List[int]]) -> List[int]:
	if matrix is None or len(matrix) == 0:
		return []
	result = []
	row_start = 0
	row_end = len(matrix)
	col_start = 0
	col_end = len(matrix[0])
	while row_start < row_end and col_start < col_end:
		# loop over 1st row left to right
		for c in range(col_start, col_end):
			result.append(matrix[row_start][c])
		row_start += 1
		# loop over Last column top-down
		for r in range(row_start, row_end):
			result.append(matrix[r][col_end -1])
		col_end -= 1
		if row_start < row_end:
			# loop over Last row right-left
			for c in reversed(range(col_start, col_end)):
				result.append(matrix[row_end -1][c])
			row_end -= 1
		if col_start < col_end:
			# loop over 1st column down-up
			for r in reversed(range(row_start, row_end)):
				result.append(matrix[r][col_start])
			col_start += 1

	return result

matr1 = [[1,2,3],[4,5,6],[7,8,9]]
matr2 = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]

print(spiral_order(matr1))
print("     ")
print(spiral_order(matr2))