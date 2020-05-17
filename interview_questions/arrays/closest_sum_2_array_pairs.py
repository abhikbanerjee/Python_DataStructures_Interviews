from typing import List


def sum_two_array_pairs(nums_a: List[int], nums_b: List[int], target_sum)-> (int, int):

	# check for base condition
	if len(nums_a) == 0 or len(nums_b)==0:
		return(0,0)

	sorted_a = sorted(nums_a)
	sorted_b = sorted(nums_b)
	i = 0
	j = len(sorted_b)-1
	target_diff = abs(sorted_a[i]+sorted_b[j] - target)
	result = (sorted_a[i], sorted_b[j])
	while i < len(sorted_a) and j >= 0:
		new_diff = abs(sorted_a[i]+sorted_b[j] - target)
		if new_diff < target_diff:
			result = (sorted_a[i], sorted_b[j])
			target_diff = new_diff
		if new_diff == 0:
			return (sorted_a[i], sorted_b[j])
		elif new_diff > 0:
			j -= 1
		else:
			i += 1
	return result

li1 = [1,3,5,6,9,15]
li2 = [2,5,7,9,10,18,22]
target = 11
print(sum_two_array_pairs(li1, li2, target))