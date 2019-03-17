

def remove_duplicates(nums):
	if len(nums) == 0:
		return []
	i, write_index = 1,1
	while i < len(nums)-1:
		if nums[i] != nums[i-1]:
			nums[write_index] = nums[i]
			write_index += 1
		i += 1
	return write_index-1


def print_arr(arr, index):
	for i in range(0, index):
		print(arr[i])


def main():
	ar1 = [1,1,2,2,3,4,5,5]
	print(print_arr(ar1, remove_duplicates(ar1)))

if __name__ == '__main__':
	main()