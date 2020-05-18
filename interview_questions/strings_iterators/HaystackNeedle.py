

def haystack_needle(haystack: str, needle: str) -> int:
	if len(needle) == 0:
		return 0
	elif haystack == needle:
		return 0
	elif len(haystack) < len(needle):
		return -1
	else:
		for i in range(0, len(haystack) - len(needle) + 1):
			if haystack[i:i + len(needle)] == needle:
				return i
		return -1


# print(haystack_needle("mississippi", "pi"))
print(haystack_needle("mississippi", "issipi"))