from typing import List


# This is a similar problem as thhe Dutch National Flag, or sort colors, using 3 pointers - LC:75
def sort_colors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <2:
            return nums
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            #loop over and swap elements depending on the value is 0 or 2
            if nums[mid]==0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # just move the mid pointer as we want the number 1 to be in the middle
                mid += 1
            elif nums[mid] == 2:
                # swap the mid and highh
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


in_li = [2,0,2,1,1,0]
sort_colors(in_li)
print(in_li)