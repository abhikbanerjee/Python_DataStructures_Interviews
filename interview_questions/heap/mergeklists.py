import heapq


def merge_k_lists(lists):
	result = []
	q = []

	# Assume there are only 2 lists
	list1_len = len(lists[0])
	list2_len = len(lists[1])

	i,j = 0,0
	while i < list1_len and j < list2_len:
		element_1 = int(lists[0][i])
		element_2 = int(lists[1][j])

		if element_1 < element_2:
			result.append(element_1)
			i += 1
		else:
			result.append(element_2)
			j += 1

	if i == list1_len:
		result.extend(lists[1][j:list2_len])
	else:
		result.extend(lists[0][i:list1_len])

	# for l in lists:
	# 	if l:
	# 		heapq.heappush(q, l.get(0))
	# for i in range(len(q)):
	# 	heapq.heappop(q)


	return result


def main():
	lists = []
	l1 = [1,3,4,6,7,9,12,14,17]
	l2 = [3,5,7,9,11]

	# l1 = [1, 3, 4, 7, 9]
	# l2 = [3, 5, 7, 9, 11]

	# l3 = [1,2,3,4]
	lists.append(l1)
	lists.append(l2)
	# lists.add(l3)

	# Call the Merge Lists function with List of Lists
	result = merge_k_lists(lists)
	print_list(result)


def print_list(list_to_print : list):
	for i in list_to_print:
		print(i)

if __name__ == '__main__':
	main()