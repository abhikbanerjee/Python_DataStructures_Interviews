from typing import List


# Find the Longest Common Prefix given a list of strings - LC:14
def longest_common_prefix(strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        longestCommonPrefix = ""
        # loop over the characters from first string and compare all strings
        index = 0
        for char in strs[0]:
            for k in range(1,len(strs)):
                print(strs[1][k])
                if index >= len(strs[k]) or char != strs[k][index]:
                    return longestCommonPrefix
            longestCommonPrefix += char
            index += 1
        return longestCommonPrefix


input1 = ["c","c"]
input2 = ["flower","flow","flight"]
# print(longest_common_prefix(input1))
print(longest_common_prefix(input2))
