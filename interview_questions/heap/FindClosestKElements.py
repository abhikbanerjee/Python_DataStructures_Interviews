import heapq


def k_closest(points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
	return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[0:K]


def k_closest_v2(points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
	# use max heap
	h_points = []
	result = []
	for point in points:
		dist = point[0]**2 + point[1]**2
		heapq.heappush(h_points, (dist, point))

	# The nearest K items are pushed to the min heap
	i = 0
	while i < K:
		item = heapq.heappop(h_points)[1]
		print(item)
		result.append(item)
		i += 1
	return result


def main():
	# points = [[1,3],[-2,2]]
	# points = [[6,10],[-3,3],[-2,5],[0,2]]
	# points = [[3, 3], [5, -1], [-2, 4]]
	points = [[6,10],[-3,3],[-2,5],[0,2]]
	K=3

	# print(k_closest(points, K))
	print(k_closest_v2(points, K))

if __name__=='__main__':
	main()