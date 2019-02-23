
def string_concatenate(my_str: str):
	if not my_str:
		return "invalid input"
	char_count = {}
	char_list = []
	result = []
	i = 0
	while i< len(my_str):
		ch = my_str[i]
		if ch not in char_count:
			char_count[ch] = 1
			char_list.append(ch)
		else:
			char_count[ch] += 1
		i += 1
	# Loop over the list
	for k in char_list:
		num_count = char_count[k]
		if num_count % 2 == 1:
			result.append(k)

	if len(result)==0:
		return "Empty String"
	else:
		return "".join(result)


#test the function
# print(string_concatenate("aabbccc"))
# print(string_concatenate("aabbbcccddb"))
# print(string_concatenate("aaabbcccdd"))
# print(string_concatenate("aabbbcccddd"))
print(string_concatenate("zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"))