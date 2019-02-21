
def summary_ranges(nums: 'List[int]') -> 'List[str]':
	i = 0
	ans = []
	while i < len(nums):
		start = nums[i]
		while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
			i += 1
		end = nums[i]
		ans.append(str(start) if start == end else "%s->%s" % (start, end))
		i += 1

	return ans


def main():
	nums_list = [0,1,2,4,5,7]
	print(summary_ranges(nums_list))

if __name__=='__main__':
	main()