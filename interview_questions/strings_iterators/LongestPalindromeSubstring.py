
def longest_palindrome_substring(s: str) -> str:
	if s is None or len(s) < 2:
		return s
	s_arr = list(s)

	# Initialize the start, end and max length variables
	start, end, max_len = 0, 0, 0

	# initialize the dp_matrix
	dp_mat = [[-1 for _ in range(len(s_arr))] for _ in range(len(s_arr))]

	# The diagonal for the dp matrix will be all 1, as a single character at every position is always a palindrome
	for i in range(len(s)):
		dp_mat[i][i] = 1

	# Initialize the dp matrix for 2 character sub-strings
	for i in range(len(s_arr) - 1):
		if s_arr[i] == s_arr[i + 1]:
			dp_mat[i][i + 1] = 1
			start = i
			end = i+1
			max_len = 2
		else:
			dp_mat[i][i + 1] = 0

	# Loop to check palindromes with str lenght 3 and above
	for sl in range(2, len(s_arr)):
		for i in range(len(dp_mat) - sl):
			# for each row, check if the first and last char are same, and the substring - leaving the first and last char are still palindrome
			if s_arr[i] == s_arr[i + sl] and dp_mat[i + 1][i + sl - 1] == 1:
				# if this is the case, the entire string is a palindrome
				dp_mat[i][i + sl] = 1
				# Store the string lengh
				if (i + sl - i + 1) > max_len:
					start = i
					end = i + sl
					max_len = sl + 1
			else:
				dp_mat[i][i + sl] = 0

	# return the longest substring
	return "".join(s_arr[start:end + 1])


inp1 = "cbbd"
print(longest_palindrome_substring(inp1))