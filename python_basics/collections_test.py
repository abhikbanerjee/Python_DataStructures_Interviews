

x = ('bear', 'cat', 'dog', 'wolf')

print(type(x))

# variable arguments being passed into functions


def varargs(*args):
	if len(args):
		for s in args:
			print(s, end=" ", flush=True)


def main():
	li = ('abc','def','ghi')
	varargs(li)
	varargs(*li)
	# Use list or tuple as arguments
	x = dict(amy=22, surbhi=33, shivangi=33, abhik=35)
	dictargs(**x)

# Use kwargs for passing in a dictionary

def dictargs(**kwargs):
	if len(kwargs):
		for k in kwargs:
			print(f'The value of {k} is {kwargs[k]}')

if __name__ == '__main__':
	main()