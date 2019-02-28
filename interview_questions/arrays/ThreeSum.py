

def three_sum(nums):
	result = []
	comp_set = {}
	non_dupl_set = set()
	for i in range(0, len(nums)):
		comp_set[nums[i]]=i

	for i in range(0, len(nums)):
		for j in range(i + 1, len(nums)):
			sum_2_nums = nums[i] + nums[j]
			if (-1*sum_2_nums) in comp_set.keys():
				val = comp_set[-1*sum_2_nums]
				if val == i or val == j:
					continue
				sol_list = [nums[i], nums[j], (-1*sum_2_nums)]
				sorted_list = sorted(sol_list)
				print(type(sorted_list))
				str_to_put = "".join([str(x)+" " for x in sorted_list])
				print(str_to_put)
				if str_to_put not in non_dupl_set:
					result.append(sorted_list)
					non_dupl_set.add(str_to_put)
	return list(result)

numbers = [-1,0,1,2,-1,-4]
print(three_sum(numbers))