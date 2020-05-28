from typing import List


def alien_dict(words: List[str], order: str) -> bool:
	alphabet = {}
	i = 0
	for char in order:
		alphabet[char] = i
		i += 1
	# print(alphabet)
	for i in range(len(words)):
		for j in range(i+1, len(words)):
			# find min between the 2 words and assign it to k
			k_range = min(len(words[i]), len(words[j]))
			for k in range(k_range):
				char_at_i = words[i][k]
				char_at_j = words[j][k]
				if alphabet[char_at_i] < alphabet[char_at_j]:
					# We can stop comparing these 2 words and continue with other words
					break
				elif alphabet[char_at_i] > alphabet[char_at_j]:
					# We know that the words are not lexicographically sorted so we can return False
					return False
				# else if its the last character and same, then we check the lengths
				elif k==k_range-1 and len(words[i]) > len(words[j]):
					return False
	return True


order1 = "hlabcdefgijkmnopqrstuvwxyz"
order2 = "worldabcefghijkmnpqstuvxyz"
order3 = "abcdefghijklmnopqrstuvwxyz"
words_set1 = ["hello", "leetcode"]
words_set2 = ["word", "world", "row"]
words_set3 = ["apple", "app"]

print(alien_dict(words_set1, order1))
print(alien_dict(words_set2, order2))
print(alien_dict(words_set3, order3))