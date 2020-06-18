

# Check if a given paranthesis String is Valid ? - LC 20
def check_paran(paran_str: str) -> bool:

	paran_stack = []
	for ch in paran_str:
		if len(paran_stack)==0:
			paran_stack.append(ch)
			continue
		if ch == ')':
			if paran_stack[-1] != '(':
				return False
			else:
				paran_stack.pop()

		elif ch == '}' != 0:
			if paran_stack[-1] != '{':
				return False
			else:
				paran_stack.pop()
		elif ch == ']':
			if paran_stack[-1] != '[':
				return False
			else:
				paran_stack.pop()
		else:
			paran_stack.append(ch)
	if len(paran_stack) == 0:
		return True
	else:
		return False


str1 = "([])[]({})"
str2 = "([)]"
str3 = "((()"

print(check_paran(str1))
print(check_paran(str2))
print(check_paran(str3))
