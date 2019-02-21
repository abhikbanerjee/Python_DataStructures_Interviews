import heapq


# Given a sorted list and 2 values k and x, find the top k elements which are the closest to the variable x

def find_closest_elements(arr: 'List[int]', k: 'int', x: 'int') -> 'List[int]':
	if len(arr) == 0 or k == 0:
		return
	while len(arr) > k:
		if abs(arr[-1]-x) >= abs(arr[0]-x):
			arr.pop()
		else:
			arr.pop(0)
	return arr


# items = [1,2,3,4,5]
items = [0,0,1,2,3,3,4,7,7,8]

m = 3
n = 5
print(find_closest_elements(items,m,n))