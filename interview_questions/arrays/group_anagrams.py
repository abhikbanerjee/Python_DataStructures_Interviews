
strs = ["eat","tea","tan","ate","nat","bat"]
anagrams_dict = {}
for word in strs:
	sorted_str = "".join(sorted(word))
	if sorted_str not in anagrams_dict.keys():
		# insert a list of this word in the values of the dict
		anagrams_dict[sorted_str] = [word]
	else:
		anagrams_dict[sorted_str].append(word)

for key in anagrams_dict.keys():
	list_words = anagrams_dict[key]
	print(key + " -> "+ ",".join([str(x) for x in list_words]))





