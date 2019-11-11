from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
	for i, elem in enumerate(numbers):
		low = i + 1
		high = len(numbers) - 1
		while low <= high:
			mid = (low + high) // 2
			if numbers[mid] == target - elem:
				return [i + 1, mid + 1]
			elif numbers[mid] > target - elem:
				high = mid - 1
			else:
				low = mid + 1
	return -1


print(two_sum([2,3,4,6,8,12], 12))
