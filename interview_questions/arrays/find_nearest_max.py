# Question - Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.
#
# For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
#
# If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.
from typing import List


def find_nearest_max(arr: List[int], index: int) -> int :
	left_pointer = index - 1 if index>=0 else -1
	right_pointer = index + 1 if index<len(arr) else len(arr)

	flag = True
	while flag:
		if left_pointer<0 and right_pointer>=len(arr):
			break
		if left_pointer>0:
			if arr[index] > arr[left_pointer]:
				left_pointer-=1
			else:
				flag = False
		if right_pointer < len(arr):
			if arr[index] > arr[right_pointer]:
				right_pointer+=1
			else:
				flag = False
	# if we reached the end and couldn't find any we just return None
	if left_pointer<0 and right_pointer>=len(arr):
		return -1
	if index == 0:
		return right_pointer
	if index == len(arr)-1:
		return left_pointer
	if abs(index-left_pointer) > abs(right_pointer-index):
		return right_pointer
	else:
		return left_pointer

def main():
	arr1 = [4, 1, 3, 5, 6]
	arr2 = [3,7,4,2,5,6]
	arr3 = [3,7,4,2,5,6]
	index1 = 0
	index2 = len(arr2)-1
	index3 = 2

	print("#####################")
	print(arr1, index1)
	print(find_nearest_max(arr1, index1))
	print("#####################")
	print(arr2, index2)
	print(find_nearest_max(arr2, index2))
	print("#####################")
	print(arr3, index3)
	print(find_nearest_max(arr3, index3))
	print("#####################")

if __name__ == "__main__":
	main()