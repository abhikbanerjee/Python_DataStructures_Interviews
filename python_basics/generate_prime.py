

def is_prime(n):
	if n <= 1:
		return False
	for i in range(2,n//2):
		if n % i == 0:
			return False
	else:
		return True


def generateprime():
	nums = 100
	for i in range(nums):
		if is_prime(i):
			print(i, end=" ", flush=True)
	print()

generateprime()
