
def n_queens(n):
	def solve_n_queens(row):
		if row == n:
			# All queens have been placed
			result.append(list(col_placement))
			return
		for col in range(n):
			# print("row-",row, " col-",col, " col-placement-", col_placement[:row], " -absolute value operation- ", [(abs(c-col),(0,row-i)) for i,c in enumerate(col_placement[:row])])
			# print("all operator - ", [all(abs(c-col) not in (0,row-i) for i,c in enumerate(col_placement[:row]))])
			if all(abs(c-col) not in (0,row-i) for i,c in enumerate(col_placement[:row])):
				col_placement[row] = col
				solve_n_queens(row+1)

	result, col_placement = [], [0]*n
	solve_n_queens(0)
	return result

# print(n_queens(2))
# print("   ")
# print(n_queens(3))
# print("   ")
print(n_queens(4))
# print("   ")
# print(n_queens(8))

# n=4
# row=0
# col_placement =  [0]*4
#
# for row in range(0,4):
# 	print(row, " - ", col_placement[:row])
# 	col=0
# 	print([all(abs(c - col) not in (0, row - i) for i, c in enumerate(col_placement[:row]))])

# print(0 not in (0,0))
# print(4 not in (0,4))