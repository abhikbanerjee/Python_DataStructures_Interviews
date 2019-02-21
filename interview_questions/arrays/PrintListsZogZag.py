# s = "PAYPALISHIRING"
# s = "PAYPALISHIRING"
s = "ABCDE"

# numRows = 3
# numRows = 4
numRows = 2

list_lists = [[] for _ in range(numRows)]

list_num = 0
go_down = True
for ch in s:
	list_lists[list_num].append(ch)
	if go_down is True:
		list_num += 1
		if list_num >= numRows-1:
			go_down = False
			list_num = numRows -1
	else:
		if list_num == 0:
			go_down = True
			list_num += 1
		else:
			list_num -= 1
st = "".join(["".join(a) for a in list_lists])
print(st)

#
# class Solution:
# 	def convert(self, s, numRows):
# 		"""
# 		:type s: str
# 		:type numRows: int
# 		:rtype: str
# 		"""
# 		if numRows == 1:
# 			return s
# 		list_lists = [[] for _ in range(numRows)]
# 		list_num = 0
# 		go_down = True
# 		for ch in s:
# 			list_lists[list_num].append(ch)
# 			if go_down is True:
# 				list_num += 1
# 				if list_num == numRows - 1:
# 					go_down = False
# 					list_num = numRows - 1
# 			else:
# 				if list_num == 0:
# 					go_down = True
# 					list_num += 1
# 				else:
# 					list_num -= 1
# 		st = "".join(["".join(a) for a in list_lists])
# 		return st