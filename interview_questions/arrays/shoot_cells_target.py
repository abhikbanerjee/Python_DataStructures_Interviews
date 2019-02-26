

def shoot_sorted_cells(matrix, target):
	results = {}
	num_rows = len(matrix)
	num_cols = len(matrix[0])

	i,j = 0,0
	while i < num_rows and j < num_cols:

