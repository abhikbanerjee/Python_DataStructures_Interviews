from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    if len(nums) < 2:
        return False
    nums_dict = {}
    for i, num in enumerate(nums):
        if num in nums_dict:
            list_pos = nums_dict[num]
            for j in list_pos:
                if abs(i - j) <= k:
                    return True
            list_pos.append(i)
            nums_dict[num] = list_pos
        else:
            new_list = [i]
            nums_dict[num] = new_list
    return False


arr1 = [1,0,1,1]
k = 1
print(contains_nearby_duplicate(arr1, k))