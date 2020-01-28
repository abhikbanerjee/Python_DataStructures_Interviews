from typing import List


def merge_interval( intervals: List[List[int]]) -> List[List[int]]:
	# print(intervals)
	intervals.sort(key=lambda x: x[0])
	print(intervals)
	merged_list = []
	for interval in intervals:
		# print(interval[0], ":", interval[1])
		if not merged_list or merged_list[-1][1] < interval[0]:
			# There is no overlap as last item is less than the start of the interval
			merged_list.append(interval)
		else:
			# There is an overlap as last item in merged list is greater than the start of the interval
			merged_list[-1][1] = max(interval[1] , merged_list[-1][1])
	return merged_list


li = [[1,3],[8,10],[2,6],[15,18]]
li1 = [[1,4],[4,5]]
li2 = [[1,3],[2,6],[8,10],[9,18]]

# print(merge_interval(li))
# print(merge_interval(li1))
print(merge_interval(li2))