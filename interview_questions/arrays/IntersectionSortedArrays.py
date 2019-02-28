

def intersect_sorted_arrays(num1, num2):
	if not num1 or not num2:
		return []
	result = []
	i,j = 0,0
	while i < len(num1) and j < len(num2):
		if num1[i] < num2[j]:
			i += 1
		elif num1[i] > num2[j]:
			j += 1
		else:
			result.append(num1[i])
			i += 1
			j += 1
	return result


number_1 = [2,4,5,6,7,9,11,12]
number_2 = [4,6,8,11,13,14,15]
print(intersect_sorted_arrays(number_1, number_2))