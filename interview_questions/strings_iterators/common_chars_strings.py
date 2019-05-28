def commonCharacterCount(s1, s2):
	common_chars = {}
	common_count = 0
	for ch in s1:
		if ch not in common_chars:
			common_chars[ch]=1
		else:
			common_chars[ch]+=1
	print(common_chars)
	for k in s2:
		if k in common_chars:
			common_count+=1
			if common_chars[k]==1:
				common_chars.pop(k)
			else:
				common_chars[k]-=1
	return common_count



s1 = "aabcc"
s2 = "adcaa"

print(commonCharacterCount(s1,s2))