from typing import List


# merge 2 sorted Arrays - LC:88
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # if no elements are present in nums2
        if n == 0:
            return
        if m == 0 and n != 0:
            # copy elements from n to m
            for i in range(n):
                nums1[i] = nums2[i]
        # take 2 pointers and start comparing and storing the results
        nums1_ptr = m-1
        nums2_ptr = n-1
        write_ptr = len(nums1)-1
        while nums1_ptr >= 0 and nums2_ptr >=0:
            if nums1[nums1_ptr] > nums2[nums2_ptr]:
                nums1[write_ptr] = nums1[nums1_ptr]
                nums1_ptr -= 1
                write_ptr -= 1
            else:
                nums1[write_ptr] = nums2[nums2_ptr]
                nums2_ptr -= 1
                write_ptr -= 1
        while nums2_ptr >= 0:
            nums1[write_ptr] = nums2[nums2_ptr]
            nums2_ptr -= 1
            write_ptr -= 1
        while nums1_ptr >= 0:
            nums1[write_ptr] = nums1[nums1_ptr]
            nums1_ptr -= 1
            write_ptr -= 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1,m, nums2, n)
print(nums1)