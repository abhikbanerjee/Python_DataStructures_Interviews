from typing import List

def checkPossibility(nums: List[int]) -> bool:
	# if len(nums) < 1:
	# 	return True
	# count = 0
	# for i in range(1, len(nums)):
	# 	if count >= 2:
	# 		return False
	# 	if nums[i - 1] < nums[i]:
	# 		continue;
	# 	else:
	# 		count += 1
	# if count < 2:
	# 	return True
	# else:
	# 	return False
	check = False
	for i in range(0, len(nums) - 1):
		if (nums[i] > nums[i + 1]) and check == True:
			return False
		elif nums[i] > nums[i + 1]:
			if i!=0 and nums[i - 1] > nums[i + 1]:
				nums[i + 1] = nums[i]
			check = True
	return True


li = [4,2,3]
li2 = [3,4,2,3]
print(checkPossibility(li))
print(checkPossibility(li2))