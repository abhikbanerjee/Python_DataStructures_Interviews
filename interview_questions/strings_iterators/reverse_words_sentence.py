import re
from typing import List


def reverse_words_sentence_1(sentence : str):
	s = re.sub(" +", " ", sentence)
	words = s.split(" ")
	reversed_str = " ".join(words[::-1])
	return reversed_str.strip()


# this does not work for multiple spaces
def reverse_words_sentence_2(sentence: str):
	rev_sent = sentence[::-1]
	rev_sent = [i for i in rev_sent]

	def reverse_word(start_char, end_char):
		while start_char < end_char:
			rev_sent[start_char], rev_sent[end_char] = rev_sent[end_char], rev_sent[start_char]
			start_char += 1
			end_char -= 1

	# final_rev_string_list = []
	start, end = 0,0
	for i in range(0, len(rev_sent)):
		if rev_sent[i] == " ":
			end = i-1
			reverse_word(start, end)
		# final_rev_string_list.append(word_ret)
	#reverse the last word
	reverse_word(start, len(rev_sent)-1)
	return "".join(rev_sent)


def reverse_words_with_spaces(s: str) -> str:
	sentence = list(s)
	def rev(words:List[str], start, end) -> List[str]:
		while start < end:
			words[start], words[end] = words[end], words[start]
			start += 1
			end -= 1
		return words
	result = []
	sent_list = rev(sentence, 0, len(sentence)-1)
	# Now reverse words and escape spaces
	i,j = 0,0
	while j < len(sent_list):
		if sent_list[i] == " ":
			i += 1
			j += 1
		elif sent_list[j] == " ":
			# found a word
			result.extend(rev(sent_list, i, j-1))
			result.append(" ")
			i = j
		else:
			j += 1
	result.extend(rev(sent_list, i, j))
	return "".join(result)

def main():
	sentence = "Hello I am Here!!"
	sentence2 = "a good   example"
	sentence3 = "the sky is blue"

	# print("Reverse words in a sentence 1 - ",reverse_words_sentence_1(sentence))
	# print("Reverse words in a sentence 2 - ", reverse_words_sentence_2(sentence))

	print(reverse_words_with_spaces(sentence))
	print(reverse_words_with_spaces(sentence2))
	print(reverse_words_with_spaces(sentence3))


if __name__=='__main__':
	main()