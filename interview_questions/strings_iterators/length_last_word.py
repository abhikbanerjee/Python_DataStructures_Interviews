import re

s = "a"


def lengthlastword(s):
	s = s.strip()
	if s == "":
		return 0
	words = s.split(" ")
	if len(words) <= 1:
		if re.search("[a-z,A-Z]", s):
			return len(s)
	else:
		return len(words[-1])

# print(lengthlastword(s))

word = "Abhik"
for i in range(0, len(word)):
	# print(word[-(i+1)])
	print(word[~i])


def check_palindrome(s):
	return all(s[i]==s[~i] for i in range(0,len(s) // 2) )

print(check_palindrome("IAMAI"))
print(check_palindrome("ABHIK"))


# Some string operations from ELP start
m = "abh" + "ik"
k = 3 * "01"

print(m)
print(k)

