from typing import List


def find_peak_element(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return 0
        else:
            return 1
    for i, num in enumerate(nums):
        print(i,num)
        if i == 0 and nums[i] > nums[i + 1]:
            return i
        elif i == len(nums) - 1 and nums[i] < nums[i - 1]:
            return i
        elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i


arr = [1,2,3]
print(find_peak_element(arr))