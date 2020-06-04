from typing import List

def generate_matrix(n: int) -> List[List[int]]:
	if n == 0:
		return []
	if n == 1:
		return [[1]]
	matrix = [[0 for _ in range(n)] for _ in range(n)]
	row_start = 0
	row_end = len(matrix)
	col_start = 0
	col_end = len(matrix[0])
	count = 1

	while row_start < row_end and col_start < col_end:
		# loop over 1st row left to right
		for c in range(col_start, col_end):
			matrix[row_start][c] = count
			count += 1
		row_start += 1

		# loop over Last column top-down
		for r in range(row_start, row_end):
			matrix[r][col_end -1] = count
			count += 1
		col_end -= 1

		if row_start < row_end:
			# loop over Last row right-left
			for c in reversed(range(col_start, col_end)):
				matrix[row_end -1][c] = count
				count += 1
			row_end -= 1
		if col_start < col_end:
			# loop over 1st column down-up
			for r in reversed(range(row_start, row_end)):
				matrix[r][col_start] = count
				count += 1
			col_start += 1
	return matrix


n1 = 1
n2 = 2
n3 = 3

print(generate_matrix(n1))
print(" ")
print(generate_matrix(n2))
print(" ")
print(generate_matrix(n3))
print(" ")
