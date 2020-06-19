from typing import List


# Find 2 numbers in a sorted array which sums to a target value LC:167
def sorted_array_2_sum(nums: List[int], target: int) -> List[int]:
    if len(nums)<2:
        return -1
    low = 0
    high = len(nums)-1
    while low<high:
        elem = nums[low]+nums[high]
        if elem==target:
            return [low,high]
        elif elem > target:
            high -= 1
        else:
            low += 1
    return -1

print(sorted_array_2_sum([2,3,4,6,8,12], 12))
print(sorted_array_2_sum([2,3,4,6,8,12], 11))
print(sorted_array_2_sum([2], 12))