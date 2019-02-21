from collections import deque

l1 = [2,4,6,7,88]
l2 = [6,8,11,15,16,18]

k = zip(l1,l2)
#
s1 = set([2,4,5,6,2])
#
d = deque()
d.append(2)
d.append(33)
d.append(21)
print(d)
d.popleft()
print(d)
d.pop()
print(d)
d.extend(l1)
print(d)
d.extendleft(s1)
print(d)
print(d.count(2))
d.reverse()
# d.remove(5)
print(d)

l1.sort(reverse=True)
print(l1)


def num_multiply(num1, num2):
	len_num1 = len(num1)
	product = 0
	for i in range(len_num1-1,-1,-1):
		power_man = len_num1-1 -i
		product += int(num1[i]) * int(num2) * (10 ** power_man)
	return str(product)

print(num_multiply("1203", "2156"))
