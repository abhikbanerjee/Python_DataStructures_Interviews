from typing import List

def removeElement(nums: List[int], val: int) -> int:
        write_index = 0
        comp_index = len(nums) -1
        while write_index <= comp_index:
            if nums[comp_index] != val:
                nums[write_index], nums[comp_index] = nums[comp_index], nums[write_index]
                write_index += 1
            else:
                comp_index -= 1
        return write_index

print(removeElement([3,2,2,3],3))