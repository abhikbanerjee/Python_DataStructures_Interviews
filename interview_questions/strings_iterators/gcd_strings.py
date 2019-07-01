
def gcd_helper(str1:str, str2: str):
	s_len = len(str1)
	t_len = len(str2)
	# base condition for recursion
	if s_len == t_len and str1!=str2:
		return ""
	# both the strings are the same, and hence this is the gcd value
	if s_len == t_len and str1==str2:
		return str1
	else:
		if len(str1) > len(str2):
			return gcd_helper(str1[t_len:], str2)
		else:
			return gcd_helper(str1, str2[s_len:])
	return gcd_helper(str1, str2)


s = "ABCABC"
t = "ABC"

print(gcd_helper(s, t))


