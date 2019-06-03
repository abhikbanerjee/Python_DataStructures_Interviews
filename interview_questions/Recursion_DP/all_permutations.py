from typing import List


def permute(nums: List[int]) -> List[List[int]]:
        def find_permutations(i):
            if i == len(nums)-1:
                result.append(nums.copy())
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                find_permutations(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        result = []
        find_permutations(0)
        return result

print(permute([1,2,3]))