from typing import List
from functools import reduce


def productExceptSelf(nums: List[int]) -> List[int]:
    if len(nums) == 0:
        return 0
    output_array = []
    i = 0
    while i < len(nums):
        if i != 0 and i != len(nums)-1:
            left_prod = reduce((lambda x, y: x * y), nums[:i])
            right_prod = reduce((lambda x, y: x * y), nums[i+1:])
            output_array.append(left_prod*right_prod)
        elif i==0:
            right_prod = reduce((lambda x, y: x * y), nums[i+1:])
            output_array.append(1*right_prod)
        else:
            left_prod = reduce((lambda x, y: x * y), nums[:i])
            output_array.append(left_prod*1)
        i+=1
    return output_array


def productExceptSelf_new(self, nums: List[int]) -> List[int]:
        table = [1 for _ in range(len(nums))]
        sofar = 1
        sofar2 = 1
        for index in range(len(nums)):
            table[index] *= sofar
            table[len(nums)-1-index] *= sofar2
            sofar *= nums[index]
            sofar2 *= nums[len(nums)-1-index]
        return table

li = [1,2,3,4,5]
print(productExceptSelf(li))
print(productExceptSelf_new(li))