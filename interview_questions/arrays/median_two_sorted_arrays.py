

def find_median_sorted_arrays(nums1, nums2) -> float:
	result = []
	if len(nums1)==0:
		result.append(nums2)
	elif len(nums2)==0:
		result.append(nums1)
	else:
		i, j = 0, 0
		while i < len(nums1) and j < len(nums2):
			if nums1[i] < nums2[j]:
				result.append(nums1[i])
				i += 1
			else:
				result.append(nums2[j])
				j += 1
		if i == len(nums1):
			result.extend(nums2[j:len(nums2)])
		else:
			result.extend(nums1[i:len(nums1)])

	# final result is sorted
	if len(result) == 1:
		return result[0]
	if len(result) % 2 == 0:
		mid = result[len(result) // 2]
		return float((result[(len(result) - 1) // 2] + result[len(result) // 2])) / 2
	else:
		return float(result[len(result)//2])

num_1 = []
num_2 = [1]
print(find_median_sorted_arrays(num_1, num_2))