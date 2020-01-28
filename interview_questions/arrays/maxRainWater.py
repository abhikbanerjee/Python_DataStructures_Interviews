from typing import List


def max_area(height: List[int]) -> int:
	area, l, r = 0, 0, len(height) - 1
	while l < r:
		area = max(area, min(height[l], height[r]) * (r - l))

		if height[l] < height[r]:
			l += 1
		else:
			r -= 1
	return area


ht = [1,8,6,2,5,4,8,3,7]
print(max_area(ht))

