from typing import List


# Given a  2D Grid, gind if a word exists or not, in the board - LC 79
def word_exist(board: List[List[str]], word: str) -> bool:
	def dfs(board, i, j, count, word) -> bool:
		if count == len(word):
			return True
		if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[count]:
			return False
		else:
			temp = board[i][j]
			board[i][j] = " "
			flag = dfs(board, i + 1, j, count + 1, word) or dfs(board, i - 1, j, count + 1, word) or \
				dfs(board, i,j - 1,count + 1,word) or dfs(board, i, j + 1, count + 1, word)
			board[i][j] = temp
			return flag

	if board is None or len(board) < 1:
		return False
	for i in range(0, len(board)):
		for j in range(0, len(board[0])):
			if board[i][j] == word[0] and dfs(board, i, j, 0, word):
				return True
	return False


board = [['A','B','C','E'],
			['S','F','C','S'],
			['A','D','E','E']]

word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"
# print(word1," : ", word_exist(board, word1))
print(" ")
print(word2," : ", word_exist(board, word2))
print(" ")
# print(word3," : ", word_exist(board, word3))
