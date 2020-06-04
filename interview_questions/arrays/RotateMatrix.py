from typing import List


def rotate_matrix( matrix: List[List[int]]) -> None:
	"""
	Do not return anything, modify matrix in-place instead.
	"""
	if matrix is None or len(matrix) == 0:
		return
	nrows = len(matrix)
	ncols = len(matrix[0])

	# Transpose the matrix first
	for i in range(nrows):
		for j in range(i, ncols):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	print("After Transpose ", matrix)

	# Swap the matrix next
	for i in range(nrows):
		k = 0
		for j in range(ncols//2):
			matrix[i][k], matrix[i][ncols - k -1] = matrix[i][ncols - k -1], matrix[i][k]
			k += 1

	print("After 90 degree rotation ", matrix)
	print(" ")
	return


mat1 = [[1,2,3],
		[4,5,6],
		[7,8,9]]

mat2 = [[ 5, 1, 9,11],
		[ 2, 4, 8,10],
		[13, 3, 6, 7],
		[15,14,12,16]]

rotate_matrix(mat1)
rotate_matrix(mat2)
