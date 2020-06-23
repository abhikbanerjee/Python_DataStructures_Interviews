# Check if a Sudoku board is valid - LC 36
from typing import List


# Check if Sudoku board is Valid - LC:36
def is_valid_sudoku(board: List[List[int]]) -> bool:
	if not board or len(board)<1:
		return False
	keep_track_list = set()
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] != ".":
				row_str = "the value " + str(board[i][j]) + " for row " + str(i)
				col_str = "the value " + str(board[i][j]) + " for col " + str(j)
				sub_grid_str = "the value " + str(board[i][j]) + " for sub grid " + str(i//3) + "," + str(j//3)
				if row_str in keep_track_list or col_str in keep_track_list or sub_grid_str in keep_track_list:
					return False
				else:
					keep_track_list.add(row_str)
					keep_track_list.add(col_str)
					keep_track_list.add(sub_grid_str)
	return True


board_val_1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board_val_3 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

board_val_2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(is_valid_sudoku(board_val_1))
print(is_valid_sudoku(board_val_2))
print(is_valid_sudoku(board_val_3))