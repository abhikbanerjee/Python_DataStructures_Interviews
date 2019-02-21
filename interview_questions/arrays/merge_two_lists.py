# Enter your code here. Read input from STDIN. Print output to STDOUT
# Given two ordered lists, define a function (merge) to return an ordered merged list.

list1 = [1, 4, 4, 5, 6]
list2 = [2, 7, 11, 11, 12, 13]


def merge(list1, list2):
	res = []
	elements_seen_so_far = set()
	# the length of the 2 lists
	len_list1 = len(list1)
	len_list2 = len(list2)
	i, j = 0, 0
	# iterate over the 2 lists until one of them finishes
	while i < len_list1 and j < len_list2:
		if list1[i] < list2[j]:
			if list1[i] not in elements_seen_so_far:
				res.append(list1[i])
				elements_seen_so_far.add(list1[i])
			i += 1
		else:
			if list2[j] not in elements_seen_so_far:
				res.append(list2[j])
				elements_seen_so_far.add(list2[j])
			j += 1

	# Merge the left out elements from the remaining list
	if i == len_list1:
		# list1 has had all the elements added to the result
		for k in range(j, len_list2):
			if list2[k] not in elements_seen_so_far:
				res.append(list2[k])
				elements_seen_so_far.add(list2[k])
				k += 1
	else:
		# list2 has had all the elements added to the result
		for k in range(i, len_list1):
			if list1[k] not in elements_seen_so_far:
				res.append(list1[k])
				elements_seen_so_far.add(list1[k])
				k+=1
	return res


def merge_no_space(list1, list2):
	res = []
	elements_seen_so_far = set()
	# the length of the 2 lists
	len_list1 = len(list1)
	len_list2 = len(list2)
	i, j = 0, 0
	# iterate over the 2 lists until one of them finishes
	while i < len_list1 and j < len_list2:
		if list1[i] < list2[j]:
			if i == 0:
				res.append(list1[0])
			if i>0 and list1[i] != list1[i-1] :
				res.append(list1[i])
			i += 1
		else:
			if j == 0:
				res.append(list2[0])
			if j > 0 and list2[j] != list2[j - 1]:
				res.append(list2[j])
			j += 1

	# Merge the left out elements from the remaining list
	if i == len_list1:
		# list1 has had all the elements added to the result
		for k in range(j, len_list2):
			if list2[k] != list2[k-1]:
				res.append(list2[k])
				k += 1
	else:
		# list2 has had all the elements added to the result
		for k in range(i, len_list1):
			if list2[k] != list2[k - 1]:
				res.append(list1[k])
				k += 1
	return res


# sorted(list1 + list2)

# print(merge(list1, list2))
print(merge_no_space(list1, list2))