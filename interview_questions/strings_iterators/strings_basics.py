

def reverse_str(str_to_rev : str):

	# One liner solution
	return str_to_rev[::-1]

	# Looping through Characters solution

	# str_len = len(str_to_rev)
	# reversed_str = []
	#
	# for i in range(str_len-1,-1, -1):
	# 	reversed_str.append(str_to_rev[i])
	# return "".join(reversed_str)


def power(n):
	return lambda a: a*n


def main():

	my_name = "My name is Abhik"
	# reverse a string
	print(reverse_str(my_name))

	# Call the lambda function for square and cube
	mydoubler = power(2)
	print(mydoubler(11))

	mytripler = power(3)
	print(mytripler(3))

if __name__ == '__main__':
	main()

