

def shoot_sorted_cells(matrix, target):
	results = {}
	num_rows = len(matrix)
	num_cols = len(matrix[0])

	i,j = 0,0
	for i in range(0,num_rows):
		for j in range(0,num_cols):
			count = 0
			if matrix[i][j] == target:
				next_i = i+1
				prev_i = i-1
				next_j = j+1
				prev_j = j-1
				# make that cell as 0
				matrix[i][j]=0

				if next_j < num_cols and matrix[i][next_j]==target:
					count += 1
					matrix[i][next_j]=0

				if prev_j > 0 and matrix[i][prev_j]==target:
					count += 1
					matrix[i][prev_j]=0

				if next_i < num_rows and matrix[next_i][j]==target:
					count += 1
					matrix[next_i][j]=0

				if prev_i > 0 and matrix[prev_i][j]==target:
					count += 1
					matrix[prev_i][j]=0

			point = (i,j)
			results[point] = count


		# return the cell values based on the sorted counts
	return sorted(results.items(), key=lambda x: x[1], reverse=True)


matr = [[2,1,3,0,2,4,5],[1,2,3,2,4,5,4],[3,2,1,0,2,4,5],[3,1,2,0,0,4,0],[0,0,1,2,3,4,5]]
print(shoot_sorted_cells(matr, 2))