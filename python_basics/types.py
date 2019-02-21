#!/us/bin/env python3

from decimal import *

# x = 7.0
# x = 7
x = None

print('x is {}'.format(x))
print(type(x))



#STRINGS
# use multiline string example

y = '''


seven


'''
print('y is {}'.format(y))
print(type(y))

# run methods on the object

m = "seven".capitalize()
n = "seven".upper()
l = "seven {} {}".format(8,9)
l1 = 'seven {1} {0}'.format(8,9)

# we can do a fill up by 8 zeros on left or right using the format
l2 = 'seven {1:<09} {0:>09}'.format(8,1234)

print(f'm is {m}')
print(f'n is {n}')
print(f'l is {l}')
print(f'l is {l1}')
print(f'l is {l2}')
print()

# NUMERIC - Use Decimal for accuracy
a = Decimal('.10')
b = Decimal('.30')

x = .1 + .1 + .1 - .3  # answer is not 0, precision is done but not accurate

y = a + a + a - b  # answer is not 0, precision is done but not accurate
print('x is {}'.format(x))
print(type(x))
print('y is {}'.format(y))
print(type(y))
print()

# SEQUENCE TYPE
x = [1,2,3,4,5] # List is an mutable sequence
x[2] = 42

for i in x:
	print(i)

print()
x1 = (1,'two',3.0,[4, '4'],5) # a tuple is not immutable
x2 = (1,'two',3.0,[4, '4'],5) # a tuple is not immutable
# x1[4] = 42   # throws an error as the tuple object is immutable

for i in x1:
	print(i)
print(type(x1))
print(type(x1[1]))

print()
# range() is not mutable, we can use a list to make it mutable
x3 = list(range(5))

for i in x3:
	print(i)

print(type(x3))


# unique ids to represent different objects
print(id(x1))
print(id(x3))

print()
print(id(x1[0]))
print(id(x2[0]))

if x1[0] is x2[0]:
	print('yep')
else:
	print('nope')

if isinstance(x1,tuple):
	print('yep its a tuple')

print()
if isinstance(x3, tuple):
		print('yep its a tuple')
else:
	print('nope its a tuple')

# Ternary operator
hungry = True

x = "Feed the Bear now " if hungry else "Dont feed the bear"
print(x)