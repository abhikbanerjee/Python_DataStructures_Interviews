

# CONDITIONAL STATEMENTS
x = 42
y = 73

if x < y:
	z = 112
	print('line 2')
	print('line 3')

elif x == y:
	print("x is equal to y")

else:
	print("value of x is greater than y")

# blocks do not define the scope of the variable (functions, objects and modules define the scope)
print(f'Value of z is {z}')

# LOOPS
words = ["one", 'two', "three", 'four']

n=0
while n < 4:
	print(words[n])
	n += 1

# fibonacci series example
a,b = 0,1
while b < 1000:
	print(b, end=' ', flush=True)
	a,b = b, a+b

print()

# for loop
for i in words:
	print(i)

# FUNCTIONS


def func(k=22):
	print(k)
	return k*2

ret_val = func(47888)
print(ret_val)

