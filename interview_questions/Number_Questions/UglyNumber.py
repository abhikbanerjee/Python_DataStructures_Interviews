

# Check if a number is ugly, if a number is divisible by 2,3 and 5 then return True else False - LC:263
def is_ugly(num: int) -> bool:
	if num == 0:
		return False
	if num % 2 == 0:
		num = num//2
		return is_ugly(num)
	if num % 3 == 0:
		num = num//3
		return is_ugly(num)
	if num % 5 == 0 :
		num = num//5
		return is_ugly(num)
	if num == 1:
		return True
	else:
		return False
