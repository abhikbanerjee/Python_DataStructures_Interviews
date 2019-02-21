#!/usr/bin/env python3

import platform


def main():
	message()
	s = 'Hello World. {}'.format(43)
	print(s)


def message():
	x = 42
	print("This is python version {}".format(platform.python_version()))
	print('Hello World. {}'.format(x))
	print(f'Hello World. {x}')  # this also works similar to the format string


# this makes sure the entire script is read before the interpreter executes the lines.
if __name__ == '__main__':
	main()
