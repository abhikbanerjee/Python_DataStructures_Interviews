from typing import List


# Get the Specific Row for a given Pascal's Triangle - LC:119
def get_row_pascal_traingle(rowIndex: int) -> List[int]:
	if rowIndex == 0:
		return [1]
	if rowIndex == 1:
		return [1, 1]
	result_set = []
	rows = [1]
	result_set.append(rows)
	for i in range(1, rowIndex):
		curr_row = []
		curr_row.append(1)
		prev_row = result_set[i-1]
		for j in range(1,i):
			curr_row.append(prev_row[j]+prev_row[j-1])
		curr_row.append(1)
		result_set.append(curr_row)
	return result_set[rowIndex-1]

print(get_row_pascal_traingle(5))