
def add_one(arr):
	if not arr:
		return
	arr[-1] += 1
	for i in reversed(range(1, len(arr))):
		if arr[i] != 10:
			break
		arr[i]=0
		arr[i-1] += 1

	# There is a carry in the last iteration
	if arr[0] == 10:
		arr[0] = 1
		arr.append(0)
	return arr


def main():
	arr_empty = [1,3,4,5,7,8]
	arr_ex_1 = [1, 3, 4, 5, 9, 9]
	arr_ex_2 = [9,9,9,9, 9, 9]
	print(add_one(arr_empty))
	print(add_one(arr_ex_1))
	print(add_one(arr_ex_2))

if __name__ == '__main__':
	main()
