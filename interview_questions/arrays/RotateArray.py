from typing import List


# Rotate Array k times - LC:189
def rotate_array(nums: List[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	if k == 0 or len(nums) < 1:
		return
	k = k % len(nums)

	def reverse(nums: List[int], start: int, end: int):
		while start <= end:
			nums[start], nums[end] = nums[end], nums[start]
			start += 1
			end -= 1

	reverse(nums, 0, len(nums) - 1)
	reverse(nums, 0, k-1)
	reverse(nums, k, len(nums) - 1)


arr = [1,2,3,4,5,6,7]
k = 3
rotate_array(arr,k)
print(arr)