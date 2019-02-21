import collections

def anagram_approach_2(word_list):
	anagram_dict = {}
	for word in word_list:
		c = collections.Counter(word)
		print(c)
		if c in anagram_dict:
			anagram_dict[c].append(word)
		else:
			anagram_dict[c] = [word]
	return anagram_dict


def main():
	word_list = ["cat", "act", "tac", "mat"]
	returned_anagrams = anagram_approach_2(word_list)
	print(returned_anagrams)

if __name__=='__main__':
	main()
