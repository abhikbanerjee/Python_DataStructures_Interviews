

def is_prefix_of_word(sentence: str, searchWord: str) -> int:
	if len(sentence) < 1 or len(searchWord) < 1 or len(sentence) < len(searchWord):
		return -1
	words = sentence.split(" ")
	for k,word in enumerate(words):
		if len(word) >= len(searchWord):
		# compare the 2 words for prefix match
			flag = True
			for i in range(len(searchWord)):
				if searchWord[i] != word[i]:
					flag = False
					break
			if flag:
				return k+1
	return -1


sentence1 = "i love eating burger"
searchWord1 = "burg"

sentence2 = "this problem is an easy problem"
searchWord2 = "pro"

sentence3 = "i am tired"
searchWord3 = "you"

sentence4 = "i use triple pillow"
searchWord4 = "pill"

sentence5 = "hello from the other side"
searchWord5 = "they"

print(is_prefix_of_word(sentence1, searchWord1))
print(" ")
print(is_prefix_of_word(sentence2, searchWord2))
print(" ")
print(is_prefix_of_word(sentence3, searchWord3))
print(" ")
print(is_prefix_of_word(sentence4, searchWord4))
print(" ")
print(is_prefix_of_word(sentence5, searchWord5))
print(" ")