import re


def reverse_words_sentence_1(sentence : str):
	re.sub("//s+", "", sentence)
	words = sentence.split(" ")
	reversed_str = " ".join(words[::-1])
	return reversed_str


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
			start = i+1
		# final_rev_string_list.append(word_ret)
	#reverse the last word
	reverse_word(start, len(rev_sent)-1)
	return "".join(rev_sent)


def main():
	sentence = "Hello I am Here!!"

	print("Reverse words in a sentence 1 - ",reverse_words_sentence_1(sentence))
	print("Reverse words in a sentence 2 - ", reverse_words_sentence_2(sentence))


if __name__=='__main__':
	main()