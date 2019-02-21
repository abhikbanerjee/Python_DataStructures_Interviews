

# This shows the use of generators, and use of iter() and next() methods - scratch sheet


# simple use of generators
# def generate_nums():
# 	for i in range(10):
# 		yield i
#
# for k in generate_nums():
# 	print(k)

# Use of Generators to not allocate everything in memory

# the usual way to allocate everything in memory


def fib(n):
	res = []
	a, b = 1, 1
	for i in range(0,n):
		res.append(str(a)+",")
		a,b = b,(a+b)
	return res

# print(fib(10000))

# the Generator way to not allocate all of it in memory


def fib(n):
	a, b = 1,1
	for i in range(0,n):
		yield a
		a,b = b, a+b

# file_f = open("/Users/abhikbanerjee/fib_file", "w")
# for k in fib(10000):
# 	file_f.write(str(k)+"\n")
# file_f.close()

	# print(k)

# Use next method to iterate over the generator func
def give_nums():
	for i in range(4):
		yield i

gen = give_nums()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# apply iter on a string
my_str = "abhik"
# print(next(my_str))

#create a iterator on the iterable my_str
it = iter(my_str)
print(next(it))
print(next(it))
print(next(it))



