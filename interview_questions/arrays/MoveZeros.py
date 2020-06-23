from typing import List


# Move Zeros to the end of the array keeping the order of non zero elements in place - LC:283
def move_zeroes(nums: List[int]) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	if len(nums) < 2:
		return nums
	# have a index which signifies the place to write
	index = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[index] = nums[i]
			index += 1
	# after coming out we need to fill all the rest of the cells with 0
	for i in range(index, len(nums)):
		nums[i] = 0


input1 = [0,1,0,3,12]
print("original array - ", input1)
move_zeroes(input1)
print("Moved Zeros - ", input1)