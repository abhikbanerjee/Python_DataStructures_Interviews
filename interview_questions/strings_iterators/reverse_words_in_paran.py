def reverseInParentheses(inputString):
	lis_input = list(inputString)
	start,end = 0, len(lis_input)
	if len(lis_input) == 0:
		return ""
	if len(lis_input) == 2 and lis_input[0] == "(" and lis_input[1] == ")":
		return ""
	if "(" not in lis_input and ")" not in lis_input:
		return "".join(lis_input)
	else:
		for i in range(len(lis_input)):
			if lis_input[i] == "(":
				start = i
			if lis_input[i] == ")":
				end = i
				break
		new_str = "".join(lis_input[0:start] + rev_str(lis_input[start+1:end]) + lis_input[end+1:len(lis_input)])
		# print(new_str)
		return reverseInParentheses(new_str)


def rev_str(str):
	str_li = list(str)
	str_len = len(str_li)
	i = 0
	j = str_len - 1
	while i < j:
		str_li[i], str_li[j] = str_li[j], str_li[i]
		i += 1
		j -= 1
	return str_li


# print(reverseInParentheses("abc(def)ghi"))
print(reverseInParentheses("abc(de(fgh))ijk"))