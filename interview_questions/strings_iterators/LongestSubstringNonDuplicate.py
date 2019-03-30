

def lengthOfLongestSubstring( s: str) -> int:
	if len(s) == 0:
		return 0
	if len(s.strip()) == 0 or len(s) == 1:
		return 1
	st = {}
	max_substr_len = 0
	running_count = 0
	i = 0
	while i < len(s):
		if not s[i] in st:
			st[s[i]]=i
			running_count+=1
		else:
			if i != len(s)-1:
				max_substr_len = max(max_substr_len, running_count)
				i = st[s[i]]+1
				running_count = 1
				st.clear()
				st[s[i]]=i
		i += 1
	return max_substr_len if running_count < max_substr_len else running_count

print(lengthOfLongestSubstring("abcb"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbb"))
print(lengthOfLongestSubstring("dvkdf"))