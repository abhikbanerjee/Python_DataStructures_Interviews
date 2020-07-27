from typing import List


# Find the meximum in a sliding window size of k : LC - 239
def max_sliding_window(nums: List[int], k: int) -> List[int]:
	from collections import deque
	result = []
	dq = deque()
	for i in range(0, len(nums)):
		# check deque is not empty and remove all elements that are not in range of k
		if len(dq) != 0 and dq[0] == i - k:
			dq.popleft()
		# remove elements which are lesser in the queue
		while len(dq) != 0 and nums[dq[-1]] < nums[i]:
			dq.pop()
		# append the current index
		dq.append(i)

		if i >= k - 1:
			result.append(nums[dq[0]])
	return result


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(max_sliding_window(nums, k))
