

def merge_sort(item_list: list):

	print("Splitting ", item_list)
	if len(item_list) > 1:

		# Calculate Mid and keep splitting
		mid = len(item_list) // 2
		lefthalf = item_list[:mid]
		righthalf = item_list[mid:]
		merge_sort(lefthalf)
		merge_sort(righthalf)

		# Now the code to merge the 2 sorted lists
		i,j,k = 0,0,0
		while i<len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				item_list[k] = lefthalf[i]
				i += 1
			else:
				item_list[k] = righthalf[j]
				j += 1
			k += 1
		while i < len(lefthalf):
			item_list[k] = lefthalf[i]
			i += 1
			k += 1
		while j < len(righthalf):
			item_list[k] = righthalf[j]
			j += 1
			k += 1
	print("merging list", item_list)
	return item_list



items = [4,6,8,10,1,2,3,11,15,18]
# items = [54,26,93,17,77,31,44,55,20]

print("Unsorted List - ", items)
print("Sorted List is ->")
sorted_items = merge_sort(items)
print(sorted_items)
