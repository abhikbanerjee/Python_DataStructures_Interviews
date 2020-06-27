from typing import List
from collections import Counter
import random
import time


def find_ranked_overlap_list(items: List[List[str]], input:List[str], overlap:int, count:int )-> List[str]:
	start = time.time()
	final_list = []
	for item in items:
		item_set = set(item)
		input_set = set(input)
		inter_set = input_set.intersection(item_set)
		# if the intersection set is greater than 0 and greater than overlap percent X
		overlap_percent = len(inter_set)*100//len(input_set)
		if len(inter_set) >= 0 and overlap_percent >= overlap:
			final_list.extend(item_set.difference(input_set))

	# we have all the elenents as part of the final list, that has overlap greater than overlap
	words_to_count = Counter(final_list)
	ret_dict = words_to_count.most_common(count)
	end = time.time()
	print("Time taken - ", (end-start))
	return ret_dict


def generate_random_data(outer_li_size, inner_list_max):
	result = []
	for i in range(outer_li_size):
		num_elements = random.randint(5,inner_list_max)
		s1 = set([chr(random.randint(65,90)) for i in range(num_elements)])
		s2 = set([chr(random.randint(97,122)) for i in range(num_elements)])
		s3 = s1.union(s2)
		#add s3 as a new list
		result.append(list(s3))
	return result




initial_list = [["a", "b", "c", "d", "e"], ["b", "e", "f", "i", "k", "m", "p", "r"],
				["a", "c", "e", "f", "k", "l", "r", "t"], ["b", "s", "t", "u", "v", "z"],
				["a", "c", "d", "k", "i", "l", "o", "p", "x", "y", "z"], ["a", "b", "e", "j", "l", "r", "z"]
]
input_list = ["a", "d", "i", "l", "r", "c", "f", "k"]
overl = 10
count_items = 2

random_data = generate_random_data(10000,50)
print(find_ranked_overlap_list(random_data, input_list, overl, count_items))




