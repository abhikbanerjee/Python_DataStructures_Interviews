def longestValidParentheses(s: str) -> int:
	ans, curMax = 0, 0
	stack = []
	for c in s:
		if c == '(':
			stack.append(curMax)
			ans, curMax = max(curMax, ans), 0
		else:
			if stack:
				m = stack.pop()
				curMax += m + 1
			else:
				ans, curMax = max(curMax, ans), 0
	print(max(curMax, ans))
	return max(curMax, ans) * 2


# str_to_test = ")()())"

str_to_test = "()(())"
print(longestValidParentheses(str_to_test))