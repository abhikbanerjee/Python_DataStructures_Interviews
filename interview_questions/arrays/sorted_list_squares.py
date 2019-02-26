

def sorted_squared_numbers(A):
	i = 0
	while i < len(A):
		if A[i] < 0:
			i += 1
		else:
			break
	res = []
	neg_arr = A[:i]
	pos_arr = A[i:len(A)]

	i, j = len(neg_arr) - 1, 0
	while i >= 0 and j < len(pos_arr):
		new_neg_nr = neg_arr[i] ** 2
		new_pos_nr = pos_arr[j] ** 2
		if new_neg_nr < new_pos_nr:
			res.append(new_neg_nr)
			i -= 1
		else:
			res.append(new_pos_nr)
			j += 1

	if i == -1:
		res.extend([k ** 2 for k in pos_arr[j:len(pos_arr)]])
	else:
		res.extend([k ** 2 for k in reversed(neg_arr[0:i+1])])
	return res


# nums = [-1,-2,-4,-6,1,2,3,4,6,7,10]
nums = [-8,-4,-1,0,3]
print("Input ", nums)
print(sorted_squared_numbers(nums))