from typing import List

def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        if len(nums1)==0:
            result.extend(nums2)
        elif len(nums2)==0:
            result.extend(nums1)
        else:
            i, j = 0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    result.append(nums1[i])
                    i+=1
                else:
                    result.append(nums2[j])
                    j+=1
            if i == len(nums1):
                result.extend(nums2[j:len(nums2)])
            else:
                result.extend(nums1[i:len(nums1)])
            #return result
        if len(result)==1:
            return float(result[0])
        elif len(result) % 2 == 0:
            return float((result[(len(result)-1)//2] + result[len(result)//2])) / 2
        else:
            return float(result[len(result)//2])


num_1 = []
num_2 = [1]
print(find_median_sorted_arrays(num_1, num_2))