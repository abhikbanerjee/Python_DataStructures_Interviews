
class Stack:
	def __init__(self):
		self.stack = []

	def push(self, key):
		self.stack.append(key)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[len(self.stack)-1]

	def print_stack(self):
		print("******** Printing Stack ******")
		for i in range(0,len(self.stack)):
			print(self.stack[i])

def main():
	#stack operations
	s = Stack()
	s.push(2)
	s.push(5)
	s.push(9)
	s.print_stack()
	s.pop()
	s.pop()
	s.print_stack()
	s.push(11)
	s.push(13)
	s.print_stack()

if __name__=='__main__':
	main()