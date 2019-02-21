import spacy
nlp = spacy.load('en_core_web_sm')

### Other dependencies
import pandas as pd
from pandas import DataFrame as df
import re


def get_grammar():
	jj_patterns = {'DT JJ', 'DT JJ NN', 'JJ', 'JJ NN', 'JJ NNS', 'JJS IN NN'}
	jj_regex = '(<DET>)*(<ADJ>)+(<ADP>)*(<NOUN>*)'

	vb_patterns = {'VB', 'VBG', 'VBG RP', 'VBN IN', 'VBN NN NN', 'VBP', 'VBP JJ', 'VBZ'}
	vb_regex = '(<VERB>+<NOUN>*<ADJ>*)'

	nn_patterns = {'DT NN', 'IN NN', 'NN', 'NN IN', 'NN NN', 'NN NNS', 'NNP', 'NNS', 'NNS IN NNS', 'PRP$ NN'}
	nn_regex = '(<DET>*<NOUN>+|<PROPN>+<ADJ>*)'

	grammar_dictionary = {'adjective': jj_regex, 'verb': vb_regex, 'noun': nn_regex}
	return grammar_dictionary


def pos_tag(text):
	return nlp(text)


def regex_chunking(spacy_doc, regex_grammar):
	''' Regex Chunk Logic
		regex match give position of match between tags and regex
		find the number and position of tags
		find the phrase using the position and number of tags
	'''
	phrases = []
	# create an index dictionary   ==  {index [word, tag]}
	index = 0
	index_dict = {}
	for token in spacy_doc:
		index_dict[index] = [token.text, token.pos_]
		index = index + 1

	# create tag string for regex match
	tags = ''.join(['<%s>' % w.pos_ for w in spacy_doc]).strip()

	# create character array of tags string = so to get all indices of '<' in tags
	char_arr = list(tags)

	# get the indices of all '<' in the tags = to count number and position of the tag while matching tag with text
	start_tag = [n for (n, e) in enumerate(char_arr) if e == '<']
	# print ("Indices of all '<': " + str(start_tag))

	for match in re.finditer(regex_grammar, tags):
		start = match.start()
		end = match.end()
		start_index = start_tag.index(start)
		end_index = start_tag.index(end) - 1
		# print (start, end)
		# print ("Indices: " + str(start_index) + "," + str(end_index))
		stringbuilder = ''
		for key, value in index_dict.items():
			if key >= start_index and key <= end_index:
				# print (key, value[0])
				stringbuilder = stringbuilder + " " + value[0]
		phrases.append(stringbuilder.strip())
	return phrases


def phrase_chunker(text, use_grammar=['adjective', 'verb', 'noun']):
	all_phrases = {}
	doc = pos_tag(text)

	if 'adjective' in use_grammar:
		adjective_phrases = regex_chunking(doc, get_grammar()['adjective'])
		all_phrases['adjective'] = adjective_phrases
	if 'verb' in use_grammar:
		verb_phrases = regex_chunking(doc, get_grammar()['verb'])
		all_phrases['verb'] = verb_phrases
	if 'noun' in use_grammar:
		noun_phrases = regex_chunking(doc, get_grammar()['noun'])
		all_phrases['noun'] = noun_phrases

	return all_phrases


def main():
	filename = 'data/resume_sample_gender.dat'
	with open(filename) as f:
		lines = f.read().splitlines()
	gender_patterns = {}
	for line in lines:
		parts = line.split(';')
		gender, job_type, text = parts[0].strip(), parts[1].strip(), parts[2].strip()
		all_phrases = phrase_chunker(text)
		for key, value in all_phrases.items():
			#             k = gender+';'+key
			#             gender_patterns[k] = value
			print(key, value)
		print('\n\n')


def read_in_pandas():
	filename = 'data/resume_sample_gender.dat'
	with open(filename) as f:
		lines = f.read().splitlines()
	d = []
	for line in lines:
		parts = line.split(';')
		d.append({'gender': parts[0].strip(), 'job_type': parts[1].strip(), 'text': parts[2].strip()})
	data = pd.DataFrame(d)
	return data

	# text = "Proven track record by Mary in manupulating isn't Science to Artistic notion of learning! The pizza was awesome and brilliant."

if __name__ == '__main__':
	main()