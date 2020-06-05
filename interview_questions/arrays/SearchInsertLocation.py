from typing import List

def searchInsert(nums: List[int], target: int) -> int:
	if nums[0] > target:
		return 0
	if target > nums[len(nums) - 1]:
		return len(nums)
	low, high = 0, len(nums) - 1
	last_loc = len(nums) - 1
	while low <= high:
		# print(low, " : ", high)
		mid = (low + high)//2
		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			high = mid - 1
			last_loc = min(last_loc, mid)
		else:
			low = mid + 1
	return last_loc

li = [1,3,5,6]
key = 7
print(searchInsert(li, key))