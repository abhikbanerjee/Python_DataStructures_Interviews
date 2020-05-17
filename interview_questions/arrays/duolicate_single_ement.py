from typing import List


def single_number(nums: List[int]) -> int:
    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    for k in nums_dict:
        if nums_dict[k] == 1:
            return k
    return -1


arr1 = [2,2,3,2]
print(single_number(arr1))