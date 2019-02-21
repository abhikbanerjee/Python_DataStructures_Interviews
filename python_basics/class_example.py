#!/usr/bin/env python3


class Duck:
	sound = 'quack'
	walking = 'Walks Like a duck !!!'

	def quack(self):
		print(self.sound)

	def walk(self):
		print(self.walking)


def main():
	donald = Duck()
	donald.quack()
	donald.walk()

	# Some string operations
	s1 = "This is a simple string operation"
	l = s1.split()
	print("---".join(l))


if __name__ == '__main__': main()