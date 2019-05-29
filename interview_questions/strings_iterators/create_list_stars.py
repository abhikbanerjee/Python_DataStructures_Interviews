
# test the * multiplied by count
len_star = 10
li = ["*"]*len_star
# print("".join(li))


# test empty list contents
xs = [()]
res = [False]*2

if xs:
	res[0] = True
if xs[0]:
	res[1] = True
# print(res)

# print string sinosodially

s = "Hello World!"
a = s[1::4]
b = s[::2]
c = s[3::4]
print(a)
print(b)
print(c)

print(a+b+c)

