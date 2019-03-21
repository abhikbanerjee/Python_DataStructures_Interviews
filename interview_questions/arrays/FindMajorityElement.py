from typing import List


def majority_element(nums: List[int]) -> int:
	elem_count = {}
	for elem in nums:
		if elem in elem_count:
			elem_count[elem] += 1
		else:
			elem_count[elem] = 1

	# sort the dict based on the counts
	sorted_dict = sorted(elem_count.items(), key=lambda x: x[1], reverse=True)
	min_amnt = len(nums) // 2
	val_to_return = 0
	for (k, v) in sorted_dict:
		if v > min_amnt:
			val_to_return = k
			break;
	return val_to_return

nums1 = [3,2,3]
print(majority_element(nums1))