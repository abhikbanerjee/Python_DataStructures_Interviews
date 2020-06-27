

# Reverse only letters - which are alphabets , and leave the other characters as they are - LC:917
def reverse_only_letters(S: str) -> str:
	if S is None or len(S) < 2:
		return S
	s_li = list(S)
	low = 0
	high = len(s_li)-1
	while low <= high:
		if not s_li[low].isalpha():
			low += 1
			continue
		if not s_li[high].isalpha():
			high -= 1
			continue
		if s_li[low].isalpha() and s_li[high].isalpha():
			s_li[low], s_li[high] = s_li[high], s_li[low]
			low += 1
			high -= 1
	return "".join(s_li)


print(reverse_only_letters("ab-cd"))
print(" ")
print(reverse_only_letters("a-bC-dEf-ghIj"))
print(" ")
print(reverse_only_letters("Test1ng-Leet=code-Q!"))
print(" ")