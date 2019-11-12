from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
	"""
	Do not return anything, modify matrix in-place instead.
	"""
	if len(matrix) == 0 or matrix[0] == 0:
		return
	rows = []
	cols = []
	for i in range(len(li)):
		for j in range(len(li[0])):
			if matrix[i][j] == 0:
				rows.append(i)
				cols.append(j)

	print(rows)
	print(cols)

	for i in range(len(li)):
		for j in range(len(li[0])):
			if (i in rows) or (j in cols):
				matrix[i][j] = 0
	return

li = [[1,1,1],
	  [1,0,1],
	  [1,1,1]]

print("Input = ", li)
setZeroes(li)
print("Output = ", li)



