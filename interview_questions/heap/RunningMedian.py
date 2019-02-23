import heapq


def median_stream(numbers):
	smaller = []
	bigger = []
	median = []
	for item in numbers:
		add_item_heap(item, smaller, bigger)
		rebalance_heaps(smaller, bigger)
		median_item = get_median(smaller, bigger)
		median.append(median_item)
	return median


def add_item_heap(item, smaller, bigger ):
	if len(smaller) == 0 or item < (-1 * smaller[0]):
		heapq.heappush(smaller,-item)
	else:
		heapq.heappush(bigger, item)


def rebalance_heaps(smaller, bigger):
	if len(bigger) - len(smaller) >= 2:
		item = heapq.heappop(bigger)
		heapq.heappush(smaller, -item)
	return


def get_median(smaller, bigger):
	if len(smaller) == len(bigger):
		return (((-1*smaller[0])+bigger[0])/2)
	else:
		# find the heap with 1 element more
		smaller_heap_elem_cnt = len(smaller)
		bigger_heap_elem_cnt = len(bigger)
		if smaller_heap_elem_cnt > bigger_heap_elem_cnt:
			return -smaller[0]
		else:
			return bigger[0]

numbers = [2,4,6,1,3,5,8,9,11,10]
print(median_stream(numbers))