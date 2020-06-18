from typing import List


# using constant space and linear time find the missing number in an array - LC 268
def missing_number(nums: List[int]) -> int:
        actual_sum = 0
        if len(nums) == 0:
            return 0
        for num in nums:
            actual_sum += num
        n = len(nums)+1
        gauzz_sum = (int)(n*(n-1))//2
        return gauzz_sum - actual_sum

input = [3,0,1]
print(missing_number(input))
